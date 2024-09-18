## Overview
This guide details the steps required to set up a pipeline in Azure DevOps that can be manually triggered to automatically deploy a built enrichment node into a target CORE-based environment.  

### Instructions
1. Create a `pipelines` directory in the root of your repo if it hasn't already been created. 
2. Copy [the example template](./files/release-pipeline-example.yml) to the `pipelines` directory in your repo. Name this according to the node for which you are creating the release pipeline, using the `.release` suffix (e.g. `enrich.zonal-nightflow.release.yml`).
3. Substitute the relevant values in the pipeline file (reference the comments in the file for more information).
4. Copy [the example docker-compose.release.yml](./files/docker-compose.release.yml) to the enrichment node directory in your repo for which you are creating the pipeline.
5. Substitute the meshnode name, docker repo and docker image name into the docker-compose file (if you haven't created an image for the node, refer to the [build pipeline creation guide](../build/Create%20Enrichment%20Node%20Build%20Pipeline.md) on how to create a pipeline for building enrichment node images). 
6. Push the resulting changes to `origin`.
7. Navigate to the `Pipelines` tab in the Azure DevOps project and click `New Pipeline`.
8. Select `Azure Repos Git` as the source for the pipeline code.
9. Select your repo from the drop down.
10. Select `Existing Azure Pipelines YAML file`.
11. Select the path to the newly created pipeline file in your repo and click `Continue`.
12. Confirm the resulting configuration by clicking `Save`.
13. Execute the pipeline manually. You will be prompted to provide the following parameters (*NB* - values that include spaces are invalid and will lead to pipeline failures):
    <br/> 
    | Parameter name | Options | Description |
    | :------------- | :--------------- | :---------- |
    | `clusterSize`  | `small`, `medium`, `large`, `xlarge`, `xlarge_gpu` | The size of the cluster to provision for the associated enrichment node. |
14. The pipeline should now be fully configured - giving the ability to manually release the latest version of the built enrichment node into a target environment.  
         
### Further resources
 - [Azure DevOps YAML schema reference](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/?view=azure-pipelines) 