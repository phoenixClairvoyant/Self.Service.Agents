## Overview 
This guide provides a quick review of the steps required to set up a pipeline in Azure DevOps that runs migrations for a PostgREST API running on an Azure App Service.

### Instructions
1. Create a `pipelines` directory in the root of your repo if it hasn't already been created.
2. Create a sub-directory for the environment in which you want to deploy the API (e.g. `development`, `sit`, `production`) if one doesn't exist 
3. Copy [the example template](./files/configure-postgrest-api.yml) to the environment sub-directory in the `pipelines` directory of your repo and name it according to the app for which you are creating the pipeline (e.g. `serve.<api-name>.migrate.yml`)
4. Substitute the relevant values in the pipeline file (reference the [Pipeline Variables Description file](./Pipeline%20Variables%20Description.md) for more detail).
5. Push the resulting changes to `origin`.
6. Navigate to the `Pipelines` tab in the Azure DevOps project and click `New Pipeline`.
7. Select `Azure Repos Git` as the source for the pipeline code.
8. Select your repo from the drop down.
9. Select `Existing Azure Pipelines YAML file`.
10. Select the path to the newly created pipeline file in your repo and click `Continue`.
11. Select `Save`.
12. Execute the pipeline   

### Further resources
 - [Azure DevOps YAML schema reference](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/?view=azure-pipelines) 