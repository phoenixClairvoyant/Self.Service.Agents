# DBT DBR-based Ingest node

* [Excellent README!!! - seriously, just go read this man...](https://dev.azure.com/exploreai/CORE.Utilities/_git/CORE.Meshnodes.BaseTemplates?path=/ingestnode_dbt/README.md&_a=preview)
* [Notion](https://www.notion.so/explore-ai/DBT-based-DBR-Ingest-Node-9c4a35c378c545bcbc6229c67b9b1c6c)
* [Developer Portal - SDKs](https://sites.google.com/sandtech.com/devportal/sdks)

Leverages DBT within Databricks for streamlined data transformations, improving quality and accelerating analytics.

## Page properties

| Property | Value | 
| --- | --- |
| Capability | Data Engineering |
| Current maintainer | kroos@sandtech.com |
| Decision records | Empty |
| Deployed ecosystems | Empty |
| Ease of reusability | Empty |
| IP Owner | Core |
| Implementer competencies required | Empty |
| Maintainer competencies required | Empty |
| Platform dependency | Empty |
| SEISE | INGEST |
| Technology dependencies | Bash, docker, Python, Cookiecutter, DBT, Databricks SQL Warehouse, ADO, Jinja2, YML |
| Type | Empty |
| Architectural Layer | Empty |


## Purpose
Engineer data like a professional.

## Inputs required

* A commitment to do data engineering like a professional.
* A desire to satisfy the need to make data better suited to enable analytics and data science.
* A plan to transform and model data.
* Skill writing SQL or PySpark to achieve the transformations.
* Basic knowledge of DBT, YML and Jinja2.
* Optionally a data set to ingest from raw flat files located in cloud storage (optional since the data could also just come from already ingested Delta Tables).
* Optionally, but ideally organise data by building a data vault or data warehouse.
* Desire to have CI CD done for you through ADO Pipelines.
* Need to have self contained deployment artifacts.
* Azure static Web hosting via Blob storage (to contain the DBT and Elementary doc sites).

## Outputs/outcomes provided

* Professionally modelled and transformed data.
* Results of data tests (through Elementary-generated site).
* Data observability (through Elementary-generated site).
* Data model and metadata documentation (through DBT generated docs site).
* Repeatable build and releases (through Azure Container Registry and ADO Pipelines).
* Deployment environment promotion (poc -> dev -> stage -> production).

## Configuration options

* If ingesting, from where to ingest (S3, ADLS Gen2, Google Cloud Storage).
* To use which Databricks Workspace, SQL Warehouse, Spark Cluster.
* When releasing, which deployment environment to target (poc, dev. stage, production).

## Deployment steps

Follow the [instructions here](https://dev.azure.com/exploreai/CORE.Utilities/_git/CORE.Meshnodes.BaseTemplates?path=/ingestnode_dbt/README.md&_a=preview).

## Maximum viable SLA
