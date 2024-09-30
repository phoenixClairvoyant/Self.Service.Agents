# Batch Load User Journey

## Scene

You've been tasked with loading the data contained in  a set of files into a cloud analytics OLAP database so that the data can drive data science efforts.
The "data science effort" is the training, evaluation and testing of a AI model that is already pioneered (proven useful and accurate).
The files are dropped in a cloud storage container on a prearranged or ad-hoc frequency, and needs to be batch loaded.
you are tasked with keeping the data as raw as possible while choosing the most appropriate data types at all times and performing the needed type conversions.
All your processes must be idempotant: running your processes twice on the same input data should not load the data twice.

In order to drive DS efforts, all raw data ingested needs to be versioned so that all DS-related preprocessing and feature engineering can always have full lineage.

Where applicable, you are tasked with modelling the data such that:

* the latest values of a given entity as well as any relationships between entities are easily obtained
* given a load date, the  values for a given entity (or relationships between entities) as they were known to be at that date are easily obtained
* for any data record it should be possible to trace it's origin back to the raw data file it was obtained from, as well as the row in the file where possible

## Persona and role

* Technical lead acting as coordinator and high-level architect
* Data engineer acting as architect and executor
* Data scientist acting as requirements generator, acceptance tester, tecnical data consultant

## Flow

This section outlines some of the principal-informed steps that should be followed in order to meet as many of the needs as possible

### Sourceing

## Example Data Details

### Scenario A: Structured and semi-structured

The files are dropped in a cloud storage container on a prearranged frequency that is currently once per day.
the files are in gzipped JSON and CSV format.
The data in the files are mostly cumulative in nature, but this is not garanteed: late arriving data may be a correction on past loaded data.

### Scenario B: Binary

The files are dropped in a cloud storage container on an indetermined  frequency that is currently whenever the manual preprocessing was performed.
the files are in TIF binary raster image format.
The data in the files are mostly cumulative in nature, but this is not garanteed: late arriving data may be a correction on past loaded data.

## Example Data Modelling Requirements

you are tasked with keeping the data as raw as possible while choosing the most appropriate data types at all times and performing the needed type conversions.
You are tasked with modelling the data such that:

* the latest values of a given entity as well as any relationships between entities are easily obtained
* given a load date, the  values for a given entity (or relationships between entities) as they were known to be at that date are easily obtained
* for any data record it should be possible to trace it's origin back to the raw data file it was obtained from, as well as the row in the file where possible

## Data Observability

You are tasked with generating a report on each data load that will:

* indicate the fresheness of the data
* surface the results of running special tests designed to verify the integrity of the data
* the integrity of the data is defined as the truthfullness of a set of assertions on the data
* surface a basic set of anomaly tests designed to attempt to detect deviation from the expected behaviour of the data

## Data Performance

For the purpose of discussion, a "direct source" of data is one that is read from a single table or view without the need for any joins or queries.
You are tasked with designing your solution such that:

* the latest values of all properties pertaining to entities (including their relationships) are direct sources
* historic point-in-time values of all properties pertaining to entities (including their relationships) for a predetermined fixed set of points in time are direct sources
* for a predetermined fixed set of intervals or windows, a predefined set of aggregations over numeric values are direct sources

## Environment Promotion

You are tasked with designing your solution such that it is straightforward to promote your solution from a poc to a dev to a stage and finally to a prod environment for each release.

## Cost Efficiency

You are tasked with creating a solution that is cost effective such that:

* it only requires compute for the duration of the load and transformation - wehn its not loading / transforming the associated compute is not running
* the compute required for retrieval of direct sources is minimal
* deterministic retrievals on direct sources are cached

## Transformation Version Control

You are tasked with keeping all code that performs transformations on data in a code version control system such as git.
It should be possible to inspect how transformation code changed from version to version.

## Solution Version Control

You are tasked with versioning your solution such that it is always possible to know what version of your solution is running.

## Solution Rollback

You are tasked withdesigning your solution such that you can, at any point in time roll back to a previously deployed version in a reasonable past time window. 

##  Gated Release

You are tasked with designing your solution such that a specific set of tests are tagged as critical, and failure in any of these tests should prevent the release.

## Metadata Management

You are tasked with generating documentation that surfaces the metadata associated with your solution.
Through browsing this metadata documentation, data scientists can understand how each table / view that you have created relates to all upstream tables, and any other special comments further describing the data.




