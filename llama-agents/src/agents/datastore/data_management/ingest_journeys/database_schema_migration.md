# Database Schema Migration User Journey

## Scene

You've been tasked with keeping the schema of  a database in sync with the latest version that the developers are working on.
The latest version of the schema is defined as the cumulative effect of running all the database migration DDL scripts in the correct order.

## Data Details

The DDL scripts are kept in a code version control system such as git.
The DDL scripts are named with an incrementing number so as to preserve the order in which they need to be run.
The DDL scripts are not allowed to change once they are committed to the code version control system.
In order to undo the effect of a past script, a new script has to be authored and executed on the database.

## Modelling Requirements

None.

## Data Observability

You are tasked with generating a report on each database migration run indicating  success / failure and which DDL scripts ran.

## Data Performance

None.

## Environment Promotion

You are tasked with designing your solution such that it is straightforward to promote your solution from a poc to a dev to a stage and finally to a prod environment for each release.

## Cost Efficiency

You are tasked with creating a solution that is cost effective such that:

* it only requires compute for the duration of the load and transformation - wehn its not loading / transforming the associated compute is not running

## Transformation Version Control

You are tasked with keeping all code that performs transformations on data in a code version control system such as git.
It should be possible to inspect how transformation code changed from version to version.

## Solution Version Control

You are tasked with versioning your solution such that it is always possible to know what version of your solution is running.

## Solution Rollback

You are tasked withdesigning your solution such that you can, at any point in time roll back to a previously deployed version in a reasonable past time window. 

##  Gated Release

You are tasked with designing your solution such that a specific set of tests are tagged as critical, and failure in any of these tests should prevent the release.

