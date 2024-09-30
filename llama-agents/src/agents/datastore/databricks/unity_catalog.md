# Databricks Unity Catalog  Notes
The Azure Learn article "[What is Unity Catalog? - Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/)"
explains that Unity Catalog (UC)is a centralised Azure Databricks data governance solution.
Key features:
* DOSE: define once, secure everywhere: single place for administering data access policies that apply across all workspaces and personas.
* Standard ANSI SQL-based security model that should be familiar to users both conceptually and syntactically:
	- use SQL syntax to grant / revoke roles and priviledges and so on.
* Built-in auditing.
* Built-in data lineage.
* Data sharing  between Databricks workspaces, even between different Databricks cloud providers.
* Even more data sharing through Delta Sharing ([Azure](https://learn.microsoft.com/en-us/azure/databricks/data-sharing/#quotas) | [AWS](https://docs.databricks.com/data-sharing/index.html)).
	- Sharing of Delta Table data and Notebooks

Note that Unity Catalog is offered on Azure and AWS, and generally there exist documentation for both.
Generally there exists feature parity, but be aware that there might be slight differences between the clouds.

## Object Model
Reference all data in Unity Catalog using a three-level namespace.

> `CATALOG.SCHEMA.{ ( MANAGED | EXTERNAL ( TABLE )) | ( VIEW ( standard | dynamic ) ) }`

## Metastore
* Top level "container" for UC.
* Persists metadata and managed tables in ADLS Gen2 storage : the associated "root" storage.
* Defined by Azure Databricks Account Admin users and assigned to workspaces.
* Existing data in the workspace can be reached at the metastore named "hive_metastore".

## Catalog
* The first of the three-part naming scheme of fully qualified identifier (FQID).
* On RDBMSs this would correspond to database, but ANSI standard referred to this as "catalog" for some time now.
* Usage permission makes catalogs visible to users.

## Schema or Database
* Azure Databricks recommends referring to this as SCHEMA and not database.
* Usage permission on the schema and catalog is required for users to see the schema, and select permission to see tables and views inside the schema.

## Table (External or Managed), view (standard or dynamic)
* Stuff that holds the data or view on the data.

### Tables
* Stored in the root storage location in delta format.

### External Tables
* Stored in any cloud storage other than the root storage location.
* Used when direct access to the data from other tools is required.
* Supports DELTA, CSV, PARQUET, ORC, AVRO, JSON, TEXT formats.

### Views (standard or dynamic)
[Create views](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/create-views#dynamic-view)

* Standard views (or simply "views") is the traditional concept of a view.
* Dynamic views provide column and row-level security (CRLS).

## STORAGE CREDENTIAL
* New first-class object introduced to contain long-term storage access credentials such as SAS tokens.

## EXTERNAL LOCATION
* New first-class object introduced to associate STORAGE CREDENTIAL and storage path.

## Limitations
* Requires Databricks Runtime 11.3 LTS.
* See "[What is Unity Catalog? - Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/)"for a full list.

## Setting up Unity Catalog
### Azure
* [Detailed instructions for Azure](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/get-started#transfer-ownership) on initial setup is provided by Azure.
* [Setting up compute that is Unity Catalog enabled](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/compute)
* SQL Warehouse is Unity Catalog enabled by default.
* [Runtime data lineage](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/data-lineage) demonstrates how you can obtain detailed, column-level data lineage - amazing!
* [Share data securely using Delta Sharing](https://learn.microsoft.com/en-us/azure/databricks/data-sharing/#quotas) explains and demonstrates how this works.

### AWS
* [Detailed instructions for AWS](https://docs.databricks.com/data-governance/unity-catalog/get-started.html) on initial setup is provided by Azure.
* Note that because the heart of the metastore is a S3 bucket, you have to pay special attention to [AWS bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).
* [Setting up compute clusters that is Unity Catalog enabled](https://docs.databricks.com/clusters/configure.html)
* SQL Warehouse is Unity Catalog enabled by default.


## Databricks Workspace and Personal Access Tokens
* Note that you need to generate a personal access token or PAT per workspace in order to get the privilege to connect to a given compute resource (SQL Warehouse for example).
* By default, users on a workspace may not have the privilege to generate a PAT, and this may have to be granted by a user with admin privileges.
* To grant users to create and use PATs, go to Admin Settings > Workspace Settings > Personal Access Tokens.
* In addition to allowing the use of PATs on the workspace, you also may need to grant individual users `use` or `manage` access  in terms of PATs.

## Cluster considerations 
Currently, only clusters with the *assigned* and *shared* access modes are compatible with Unity Catalog.
Consult:

-  [this page for Azure](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/compute)
- and [this page for AWS](https://docs.databricks.com/data-governance/unity-catalog/compute.html) for full details on the requirements Unity Catalog impose on a cluster.

 ## Usage Examples
We assume you are using the Core DBT-based ingest node for Databricks.
During the `cookiecutter` setup you would have been prompted for a couple of parameter values that form part of the `.env` file configuration.
However, for security reasons, the `cookiecutter` setup would not have prompted you for a PAT, so you have to manually add that to the `.env` file.

To test Unity Catalog access, revoke/grant privileges you would dneed the PAT to a user that has admin privileges on the workspace,
as well as a PAT for another user with workspace access only.

First we will check that the workspace access PAT cannot view or use catalogs.
When we confirmed this, we will use the admin PAT to grant access and then confirm that we now have access on the workspace access PAT.
After you have added the workspace access PAT to the  `.env` file, proceed as per usual:

```bash
# go to where your ingest node was setup
cd ingest/bridgetown_uc1/
. .bash_aliases
ingest-acr-login
ingest-pull
ingest-build
ingest-dbsqlcli
```

Now you should be connected to the Serverless SQL Warehouse for the particular workspace.
From here you will execute SQL commands to check access to and to grant/revoke access.

Note: if you are not using the Core DBT-based ingest node for Databricks, you can also connect through DBeaver or directly in the workspace.

```sql
show catalogs; -- should not show you catalogs you do not yet have access to / admin can see everything
use catalog bridgetown_uc1;-- some catalog you want to use
show schemas;
use schema bridgetown_uc1_seed_data; -- some schema you want to inspect
show tables;
```

Depending on if the user associated with the PAT had access or not the above statemens will pass/fail.

Here are some example statements to grant/revoke privileges.

```sql
show users;
show catalogs;
grant use catalog on catalog bridgetown_uc1 to `hlosani@explore-ai.net`;
use catalog bridgetown_uc1;
show schemas;
grant use schema on schema bridgetown_uc1_seed_data to `hlosani@explore-ai.net`;
use schema bridgetown_uc1_seed_data;
show tables;
grant select on table tags to `hlosani@explore-ai.net`;
revoke all privileges on catalog bridgetown_uc1 from `hlosani@explore-ai.net`;
```

Notice how the user is specified through back quotes.

See also:
* [GRANT statement](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/security-grant)
* [REVOKE statement](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/security-revoke)
*  [Privileges and securable objects](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/privileges)

