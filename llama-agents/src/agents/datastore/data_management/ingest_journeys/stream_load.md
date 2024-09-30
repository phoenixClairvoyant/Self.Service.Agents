# Streaming Load User Journey

## Scene

You've been tasked with near real-time loading of data being streamed into a couple of Kafka topics.

## Data Details

The data is published to the Kafka topics as soon as it is available.
the data is IoT / sensor data in JSON format.
you are tasked with keeping the data as raw as possible while choosing the most appropriate data types at all times and performing the needed type conversions.
The data in the topics are only cumulative in nature.
All your processes must be idempotant: running your processes twice on the same input data should not load the data twice.

## Modelling Requirements

You are tasked with modelling the data such that:

* the latest values of a given entity as well as any relationships between entities are easily obtained
* given a load date, the  values for a given entity (or relationships between entities) as they were known to be at that date are easily obtained

## Data Observability

You are tasked with serving a report on  the current state of data load that will:

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

You are tasked with designing your solution such that it is straightforward to promote your solution from a poc to a dev to a stage and finally to a prod environment.

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

