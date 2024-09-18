
/*
 * Simple demo of hub, satellite and link DDL and DML.
 * The pattern is more 'ELT' than 'ETL' so extract, transform and load, with operations happening in the database.
 * It is also perfectly acceptable and desireable to do the hash generation in Airflow for example, as part of the extract.
 * 
 * This is the simplest possible vault: one hub  for tag_names, one link for measurement events, one satellite for recording the measurement value.
 * Usually, links would have more than one hub.
 * Another way to model this data would be a satellite directly on the hub. 
 * 
 * Main assumptions and conventions (return here after reading the rest of the file):
 * 1. Hashing via SHA256 and representing via 64 chars hex encoded.
 * 2. If space is a concern, 32 byte binary type could be used instead, but only do this if really required.
 * 3. For concatenation seperator use pipe symbol: '|' 
 */

/*
 * DDL
 */

-- for illustration purposes - can drop afterwards
create schema if not exists data;
create schema if not exists raw;

CREATE EXTENSION IF NOT EXISTS pgcrypto; -- for the digest function for sha256 hashing

-- hub : this is the ultimate destination for the tag names
drop table if exists data.tag_hub; 
create table data.tag_hub (
_hashkey char(64)not null primary key,
_loaddatetime timestamp with time zone  not null default(current_timestamp),
_originsource varchar(256) null,
tag_name varchar(256)
);
comment on table data.tag_hub is 'this is the ultimate destination for the tag names';

-- link : represents the fact that a measurement event occured - a measurement reported by a sensor
drop table if exists data.tag_measurement_link ; 
create table data.tag_measurement_link (
_hashkey char(64)not null primary key,
_loaddatetime timestamp with time zone  not null default(current_timestamp),
_originsource varchar(256) null,
measurement_timestamp timestamp with time zone  not null,
tag_hub_hashkey char(64)
);
comment on table data.tag_measurement_link is 'represents the fact that a measurement event occured - a measurement reported by a sensor';

-- satellite : represents the value(s) of a measurement event - a measurement reported by a sensor
drop table if exists data.tag_measurement_satellite ; 
create table data.tag_measurement_satellite (
_hashkey char(64)not null,
_hashdiff char(64)not null,
constraint pk_tag_measurement_satellite primary key (_hashkey, _hashdiff),
_loaddatetime timestamp with time zone  not null default(current_timestamp),
_originsource varchar(256) null,
measurement_value float not null
);
comment on table data.tag_measurement_satellite is 'represents the value(s) of a measurement event - a measurement reported by a sensor';

/*
 * Raw ingestion and staging layers
 */

-- this table represents the data as raw as it gets, and reflects the source - in this case the raw pitag data
drop table if exists raw.pitag_import;
create table raw.pitag_import (
measurement_timestamp timestamp with time zone not null, 
tag_name varchar(256) not null, 
measurement_value float
);
comment on table raw.pitag_import is 'this table represents the data as raw as it gets, and reflects the source - in this case the raw pitag data';

/*
 * DML
 */

-- some data to test with
-- this would be loaded from a file if batch, or streamed in, or via Airflow or any other ingest
-- 9 values for 3 tags
-- you can comment out with double-dashes  some of the lines here to test that rows are added/not added respectively
-- You can also add rows here to test the other queries.
-- truncate table raw.pitag_import;
insert into raw.pitag_import values 
('2021-06-01 00:00:00+00:00','TRNSF:10314-FLOW',-3.4398494),
('2021-06-01 00:15:00+00:00','TRNSF:10314-FLOW',-3.7218046),
('2021-06-01 00:30:00+00:00','TRNSF:10314-FLOW',-3.6090226),
('2021-06-01 00:00:00+00:00','DLM:14336-FLOW',29.162193),
('2021-06-01 00:15:00+00:00','DLM:14336-FLOW',28.67884),
('2021-06-01 00:30:00+00:00','DLM:14336-FLOW',27.416758),
('2021-06-01 00:00:00+00:00','TRNSF:30784-FLOW',-0.07955077),
('2021-06-01 00:15:00+00:00','TRNSF:30784-FLOW',-0.07945796),
('2021-06-01 00:30:00+00:00','TRNSF:30784-FLOW',-0.08040857)
;

-- the purpose of a staging table is to  compute the hashes once
-- the staging table is not meant to be a place  to alter any of the raw values, but to compute additional things: mainly hashes
-- note that these hashes could also accompany the raw data, and it makes sense to compute it outside of the db, say via Airflow, to spare the db of this chore
-- If computed outside via Airflow it is very important to set standards of exactly how the hashes should be computed.
-- If the hashes are computed upfront, they could accompany the first-time data ingest rather than requiring an update, which is far slower.
-- staging table data, like import raw data is never the ultimate destination and the tables could be truncated at any time
drop table if exists raw.pitag_staging;
create table raw.pitag_staging(
measurement_timestamp timestamp with time zone not null, 
tag_name varchar(256) not null, 
measurement_value float,
_tag_hashkey VARCHAR(64) not null,
_measurement_hashkey VARCHAR(64) not null,
_measurement_hashdiff VARCHAR(64) not null
);
comment on table raw.pitag_staging is 'the purpose of a staging table is to  compute the hashes once, since they might be used more than once - note that this table is ephemeral and will be truncated at any time';

-- now we compute the hashes once and use it multiple times
insert into raw.pitag_staging (measurement_timestamp, tag_name, measurement_value, _tag_hashkey, _measurement_hashkey, _measurement_hashdiff)
select 
p.measurement_timestamp, p.tag_name, p.measurement_value, 
encode(digest(p.TAG_NAME, 'sha256'), 'hex') as _tag_hash_key,
encode(digest(
concat_ws('|', 
p.measurement_timestamp, 
encode(digest(p.TAG_NAME, 'sha256'), 'hex')),
'sha256'), 'hex')
as _measurement_hashkey,
encode(digest(concat_ws('|', p.measurement_value), 'sha256'), 'hex') as _measurement_hashdiff
from raw.pitag_import as p;
/*
 * Notice how we compute a straight hash of the tag_name for _tag_hashkey, but
 * we concatenate (with '|'as seperator, which is just a convention), both the measurement_timestamp and hash of the tag_name for _measurement_hashkey.
 * _measurement_hashkey represents the key for when a mesurement took place, so if ever in future we receive a duplicate measurement for same tag and timestamp, we can ensure uniqueness (if we desire to do so).
 * For _measurement_hashdiff we compute the hash over the measurement_value only, because this will enable us to track changes. 
 * If we had more mesurements for the given timestamp, we would concat them with '|'and then compute the hash.
 */


/*
 * Final step: insert into the vault
 */

--- and now we insert into the hub, being mindful of _hashkey values that might be there already
-- this pattern, of joining on to the existing data to prevent duplicates is the norm since most (if not all) cloud analytics databases do not support uniqueness constraints
insert into data.tag_hub 
(
_hashkey,  _loaddatetime, _originsource, tag_name 
)
select distinct 
p._tag_hashkey, current_timestamp , 'raw.pitag_staging', p.tag_name
from raw.pitag_staging as p 
where p._tag_hashkey not in (select _hashkey from data.tag_hub)
;

-- and we can demonstrate that the hub only has one _loaddatetime per batch loaded
select count(distinct _loaddatetime) from data.tag_hub;

/*For the link, the record of a measurement event having taken place, we do not care about uniqueness of the _hashkey because we have the _loaddatetime to
 * identify the latest event by.
 * If we want to prevent more than one measurement, for a given tag, at a given time, we could check for uniqueness - see below for an example of this - but usually this would not be the case for event data.
 * It might also be good to not check for uniqueness but rather inspect the data regularly : if a lot of duplicates are being received that might be a problem in itself.
 */ 
insert into data.tag_measurement_link (
_hashkey,
_originsource,
measurement_timestamp,
tag_hub_hashkey
)
select
_measurement_hashkey,
'raw.pitag_staging',
measurement_timestamp ,
_tag_hashkey
from raw.pitag_staging as p 
;

-- and here is an example of how to force uniqueness if required
insert into data.tag_measurement_link (
_hashkey,
_originsource,
measurement_timestamp,
tag_hub_hashkey
)
select
_measurement_hashkey,
'raw.pitag_staging',
measurement_timestamp ,
_tag_hashkey
from raw.pitag_staging as p 
where p._measurement_hashkey not in (
select distinct _hashkey  
from  data.tag_measurement_link 
);

/*
 * Finally we insert for the actual measurements, and here we tie back to the link, since we are recording attributes on the event.
 */ 
 insert into data.tag_measurement_satellite (
_hashkey,
_hashdiff, 
_originsource,
measurement_value 
)
select -- new measurements
_measurement_hashkey,
_measurement_hashdiff,
'raw.pitag_staging',
measurement_value 
from raw.pitag_staging as p 
where _measurement_hashkey   not in (
select distinct _hashkey  from data.tag_measurement_satellite
)
union all
select -- updated measurements
_measurement_hashkey,
_measurement_hashdiff,
'raw.pitag_staging',
p.measurement_value 
from raw.pitag_staging as p 
join data.tag_measurement_satellite as s 
on p._measurement_hashkey = s._hashKey 
and p._measurement_hashdiff <> s._hashdiff
;

