# Pull vs push architecture for ingest on PostgreSQL with the COPY statement

* Should data in the 10's of GB, 10's of millions of rows be considered large and slow to ingest in 2024?
* "Middlemannietjie" or "Piggy-in-the-middle" is a game kids play:
	- Two kids (Shaun and Aidan) throw a ball between them, and a third kid (Kevin) tries to catch the baal in mid flight.
* A lot of our ingest work in Sand follows this pattern:
	- Structured data (CSV) sits in S3 (Shaun).
	- Python notebooks with Pandas, or maybe PySpark on a Spark cluster reads this S3 data (Kevin).
	- The data needs to go into a PostgreSQL db (Aidan) so Kevin writes it there.
* Problem with this is that Kevin becomes the bottleneck, and has to negotiate a lot of things:
	-rate at which Shaun can supply the data
	- rate at which Aidan can store the data
	- buffering the data
	- fighting off the temptation to correct/alter the data (transformations)
	- Kevin needs a place to compute
* All of this makes it a huge challenge for engineers since they have to chunk and buffer and load files to a local storage etc.
* An alternative is to use a pull architecture where Aidan asks Shaun to throw the ball when he is ready.
* All the big cloud analytics OLAP databases (Snowflake, BigQuery, RedShift, DBR SQL Warehouse) operate like this with variations of a COPY SQL statement.
* PostgreSQL traditionally supported a COPY statement to ingest files directly from the disk accessible to the server.
	- This cannot work for S3 obviously.
* PostgreSQL COPY statement at some point got a PROGRAM clause, which would make it call a program executable by the server, on the server!
	- This PROGRAM can be anything, so why not something that can stream from S3?
* We bundled the MinIO mc CLI binary into our Postgres image, and made it so that the running server can execute it.
	- Ingest is now a couple of lines of code vs the old whole script or notebook.
	- Ingest that took half a day now takes ~10 minutes.
	- Ingest that did not even terminate now takes ~10 minutes.
	- Ingest under the best of conditions (file is on fs on VM, script runs on VM)that took 35 minutes now takes 10 minutes and is much simpler.


Some comments from the Telco team:

> Just noting that the most recent ingestion was done locally, not from VM/Minio. Took around 5 minutes to load and ~30 minutes to write (the 60 million, ~14GB Google buildings CSV).
> VM/Minio (reading in chunks) - failed to load from Minio.
> local/Minio (reading in chunks) - ran for hours and had to terminate.

## How to do it?

### Videos!

To assist you incorporating this technique in your data engineering toolbox I have created the following video guides:

* [Pull Ingest from S3-compatible storage to PostgreSQL - Part 1](https://drive.google.com/open?id=1C1frYNCHAtEddNrwHC25W391H4mFl_5C&usp=drive_fs)
* [Pull Ingest from S3-compatible storage to PostgreSQL - Part 2](https://drive.google.com/open?id=1-2ZuT-1q1p8m63sSjn1vcWzbrK_6lzZE&usp=drive_fs)

Please let us know [on our Dev Platform](https://sites.google.com/sandtech.com/devportal/home) if this has been useful to you, or if you have any other comments or suggestions.

1. Build or obtain a PostgreSQL docker image that has Minio mc CLI bundled in.
	- The mc CLI command must be executable by the OS user that runs the postgres daemon.
1. Connect to the database where the ingest should happen as a privileged role (usually the `postgres` user) who can grant the `pg_execute_server_program` privilege.
1. As such a privileged role, grant the role that will do the actual ingest this [pg_execute_server_program](https://www.postgresql.org/docs/current/predefined-roles.html) privilege:
	- `grant pg_execute_server_program to role ingestion_user;`
1. Now connect to the database where the ingestion should happen, as the role that will do the ingestion.
1. Next make a schema and table to hold the new staged raw data.
	- Note that this table has to follow exactly the format of the file to be ingested, so you first need to figure out how exactly this data looks. More on this later.
1. After the schema and table has been created to support the format of the file to be ingested, when loaded with the `COPY ... FROM PROGRAM ..` statement it is time to do the ingest!
1. To perform the ingest with the `COPY ... FROM PROGRAM ...` statement, obtain the S3-compatible credentials:
	- S3_ACCESS_KEY
	- S3_SECRET
	- S3_SESSION_ID (if applicable)
1. Now, craft a [COPY ... FROM PROGRAM ...](https://www.postgresql.org/docs/current/sql-copy.html) statement to perform the ingest, and execute it.
	- Note that the `FROM PROGRAM` clause can be anything that can be executed by the OS user that the postgres daemon runs as.
	- Note that we make use of the [mc cat .. command](https://min.io/docs/minio/linux/reference/minio-mc/mc-cat.html), so the `mc` command, and the `cat` verb/option, which will stream to stdout, which will get picked up by postgres.
	- The `FROM PROGRAM` clause can accept a bash statement, so you can set once-off environment variables if required.
	- Since it is a bash statement, you could in theory pipe to `cut` or `awk` to only select specific columns, or decompress and so forth.
1. While it is executing you can query the [pg_stat_progress_copy](https://pgpedia.info/p/pg_stat_progress_copy.html) view to see how the process is progressing.
	- `select * from pg_stat_progress_copy;`
1. Note that this method of ingest is definately not only limited to  CSV formatted input: it can handle JSON or any other format provided you can have the final output of the streamed data conform to something PostgreSQL can work with.
1. Furthermore, this method is not limited to ingress but also egress, so you can use this to dump data out to S3-compatible storage.
	- For more details, see the [COPY ... FROM PROGRAM ...](https://www.postgresql.org/docs/current/sql-copy.html) documentation.

## Example SQL

```sql
-- connect as postgres user on the db you would like to target, grant the role 
grant pg_execute_server_program to ingestion_user;

create schema if not exists stage;

grant all on
schema stage to ingestion_user;

select
	*
from
	pg_stat_progress_copy;

-- connect to the db where you want to ingest as the user you want to ingest as
set search_path=stage,public;
create table buildings_csv (
	latitude float,
	longitude float,
	area_in_meters float,
	confidence float,
	geometry text,
	full_plus_code text
);

COPY buildings_csv (
	latitude,
	longitude,
	area_in_meters,
	confidence,
	geometry,
	full_plus_code
)
FROM PROGRAM 'MC_HOST_source=''http://<s3-access-key>:<s3-secret-key>:<s3-session-id-optional>@10.4.13.4:9000'' /opt/bin/minio-binaries/mc cat source/eai-telco-mtn-poc-eu-west-1-dev-s3-data/raw_data/Indonesia/google_buildings/2e7_buildings.csv'
WITH (FORMAT CSV , HEADER, QUOTE '"', DELIMITER ',' );
```

## Dockerfile help

If you are unlucky in that  you don't already have a nice PostgreSQL from Core with these tools installed for you, don't worry, we are here to help!
Below is part of a `Dockerfile` that, if added to your PostgreSQL `Dockerfile` will enable it with `curl` and `mc`.

```bash
# Install additional tools that postgres might need for ingest and other tasks, in particular curl and mc, to achieve the COPY .. PROGRAM style inges
#  https://www.postgresql.org/docs/current/sql-copy.html
RUN apt-get update && apt-get install -y curl

# install MinIO mc CLI for use in the COPY statement's PROGRAM clause
RUN curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  --create-dirs \
  -o /opt/bin/minio-binaries/mc

RUN chmod a+rx /opt && \
    chmod a+rx /opt/bin/ && \
    chmod a+rx /opt/bin/minio-binaries/ 

RUN chown postgres:postgres /opt/bin/minio-binaries/mc
RUN chmod 755 /opt/bin/minio-binaries/mc
RUN export PATH=$PATH:/opt/bin/minio-binaries/
RUN echo 'export PATH=$PATH:/opt/bin/minio-binaries/' >> ~/.bashrc
```


## Oh, this all seems very nice, but I am on a DaaS (db as a service) on the cloud...

* AWS: Don't fear! If you are on AWS RDS for example, you have access to the [aws_s3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.S3Import.html) PostgreSQL extension, with which you can implement a similar PULL INGEST architecture!
* Azure: Don't fear If you are on Azure Flexible Server for Postgres you have access to the [azure_storage](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-storage-extension) PostgreSQL extension, with which you can implement a similar PULL INGEST architecture!
