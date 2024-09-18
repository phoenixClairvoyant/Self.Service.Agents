### Instructions
1. Create a `pipelines` directory in the root of your repo if it hasn't already been created
2. Copy [the example template](./files/dbt/build-pipeline-example.yml) to the `pipelines` directory in your repo and name it according to the node for which you are creating the build pipeline with the `ingest.build` prefix (e.g. `ingest.build.environmental-ingest.yml`)
3. Substitute the relevant values in the pipeline file (Reference the comments in the file for more information)
4. Navigate to the `Pipelines` tab in the Azure DevOps project and click `New Pipeline`
5. Select `Azure Repos Git` as the source for the pipeline code
6. Select your repo from the drop down
7. Select `Existing Azure Pipelines YAML file`
8. Select the path to the newly created pipeline file in your repo and click `Continue`
9. Select `Save`
10. Execute the pipeline manually, or update the code for the relevant node to trigger the build pipeline 

### Further resources
 - [Azure DevOps YAML schema reference](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/?view=azure-pipelines) 