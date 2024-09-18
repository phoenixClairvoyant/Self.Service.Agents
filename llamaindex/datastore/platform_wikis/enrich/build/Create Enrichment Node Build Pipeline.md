## Overview 
This guide provides a quick review of the steps required to set up a pipeline in Azure DevOps that automatically tests and builds any changes made to a target enrichment node. The enrichment node images get pushed to the default container registry that is created within a given environment.

### Instructions
1. Create a `pipelines` directory in the root of your repo if it hasn't already been created.
2. Create a sub-directory for the environment in which you want to deploy the node (e.g. `sit`, `production`) if one doesn't exist 
3. Copy [the example template](./files/build-pipeline-example.yml) to the environment sub-directory in the `pipelines` directory of your repo and name it according to the node for which you are creating the build pipeline (e.g. `enrich.zonal-nightflow.build.yml`)
3. Substitute the relevant values in the pipeline file (reference the [Pipeline Variables Description file](./files/Pipeline%20Variables%20Description.md) for more detail).
4. Push the resulting changes to `origin`.
5. Navigate to the `Pipelines` tab in the Azure DevOps project and click `New Pipeline`.
6. Select `Azure Repos Git` as the source for the pipeline code.
7. Select your repo from the drop down.
8. Select `Existing Azure Pipelines YAML file`.
9. Select the path to the newly created pipeline file in your repo and click `Continue`.
10. Select `Save`.
11. Execute the pipeline manually, this should invoke permission requests to authorise Azure to automatically call processes on your behalf. 
12. Your pipeline is now configured. You can automatically trigger it by pushing updates of the code associated with the relevant target node directory. Alternatively, you can manually run the pipeline (convenient when trying to perform debugging) using the Azure Devops console.    

### Further resources
 - [Azure DevOps YAML schema reference](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/?view=azure-pipelines) 