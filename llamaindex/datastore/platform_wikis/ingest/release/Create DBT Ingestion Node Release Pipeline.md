### Instructions
1. Create a `pipelines` directory in the root of your repo if it hasn't already been created
2. Copy [the example template](./files/dbt/release-pipeline-example.yml) to the `pipelines` directory in your repo and name it according to the node for which you are creating the release pipeline with the `ingest.release` prefix  (e.g. `ingest.release.environmental-ingest.yml`)
3. Substitute the relevant values in the pipeline file (Reference the comments in the file for more information, and contact the CORE team for the relevant Snowflake-related information)
4. Copy [the example docker-compose.release.yml](./files/snowsqlcli/release-pipeline-example.yml) to the ingestion node directory in your repo for which you are creating the pipeline
5. Substitute the meshnode name, docker repo and docker image name into the docker-compose file (if you haven't created an image for the node, refer to the [build pipeline creation guide](../build/Create%20DBT%20Ingestion%20Node%20Build%20Pipeline.md) on how to create a pipeline for building ingestion node images)
6. Navigate to the `Pipelines` tab in the Azure DevOps project and click `New Pipeline`
7. Select `Azure Repos Git` as the source for the pipeline code
8. Select your repo from the drop down
9. Select `Existing Azure Pipelines YAML file`
10. Select the path to the newly created pipeline file in your repo and click `Continue`
11. Select `Save`
12. Execute the pipeline manually. You will be prompted to provide the following parameters (**NB** - values that includes spaces are invalid and will lead to pipeline failures):
    <br/> - `deploymentEnvironment` -> the environment in which the DB is hosted (`development`, `prod`, etc.)
    <br/> - `isInitialRelease` -> boolean value indicating if this is the initial release of the node. **NB** - If this is set to `true` after the initial release, it will result in a loss of data
    <br/> - `databaseName` -> the name of the Snowflake database used for the DBT vault
    <br/> - `databaseSchemaName` -> the name of the database schema to be used

### Further resources
 - [Azure DevOps YAML schema reference](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/?view=azure-pipelines) 