## Overview 
This guide provides an overview of the steps required to set up a pipeline in Azure DevOps to deploy a base CORE environment

### Instructions
1. Create copies of the Terraform variable files in the [`variable-files` directory](./variable-files/) and rename them according to the following convention: `<team_name>.<use_case>.<deployment_environment>.<resource_name>.tfvars`,<br/> where each value represents the following:
**!! JG: Where should the copy of these files be stored? CORE.Platform?** 
  - Values that include spaces are invalid. The variable files are already named according to the resources to which they map.  
  - The file names should be lowercase
1. Update variable files with relevant values (refer to [Variable Description guide](./Variables%20Description.md) for more detail) **!! JG: Need to check that there is full alignment with these lists** 
2. Create a copy of the backend config file in the [`terraform-remote-backend-config` directory](./terraform-remote-backend-config/config.azurerm.tfbackend) and rename them according to the same convention as above: `<team_name>.<deployment_environment>.config.azurerm.tfbackend`  
3. Upload the newly created files to the [Azure DevOps Pipelines Library in the `CORE.Platform` project](https://dev.azure.com/exploreai/CORE.Platform/_library?itemType=SecureFiles)  
4. Update the `teamName` and `useCase` parameters in the [environment provisioning pipeline](https://dev.azure.com/exploreai/CORE.Platform/_git/CORE.Platform?path=/provision/environment.yml) with the name of the team and the use case  
5. Execute the pipeline, selecting the team name, use case and deployment environment according to the values used in previous steps  
6. For each stage of the pipeline, grant access to the secure files used for provisioning each individual resource (this is only necessary on the first pipeline execution or if a new version of the secure file is uploaded)
    <br/>
    <br/>
    | Parameter name | Description |
    | :------------- | :---------- |
    | `Team Name` | The name of the team for whom the environment is being provisioned. (e.g. `severntrent`, `southernwater`, `digitaltwins`) | 
    | `Use Case`  | The use case that the team is tackling |
    | `Deployment Environment`  | Target environment into which the node should be deployed. Accepted values: `demo`, `poc1`,`development`, `sit`, `production` |
    | `Allow Destructive Changes`  | Whether or not Terraform should be allowed to make destructive changes to resources |
    **!! JG: The last param - `Allow Destructive Changes` is not present in the naming convention, how should this be included?** 

### Required Permissions
* Read permissions on [EXPLORE.CORE key vault](https://portal.azure.com/#@explore-ai.net/resource/subscriptions/abc4c8b4-2e98-48b3-ac23-17498266f10f/resourceGroups/EXPLORE.CORE/providers/Microsoft.KeyVault/vaults/explore-core-development/overview)


### Common Failures
* Hung pipeline
    * At times the pipeline will hang on a certain stage without throwing an error. This is usually due to the value for a required variable not present in the files uploaded to Azure DevOps.
    * This is the default Terraform behaviour. When a file is passed that provides the values for the variables required for a given script, and no default value is specified, Terraform will expect the value for that variable to be specified via the CLI at runtime. This is not possible to do in an Azure DevOps pipeline, which results in the execution pausing while waiting for input
    * Resolution: Cancel the pipeline execution, add the missing variable to the variable file (can be determined based on which stage of the pipeline hung) and reupload the file. Reuploading a secure file requires deleting the existing copy of a given file and then uploading the new version. Azure DevOps does not secure updating uploaded files.