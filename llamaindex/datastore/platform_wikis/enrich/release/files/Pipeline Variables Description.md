## Pipeline Variables
* `armServiceConnectionEndpoint`
    - The service endpoint used by Azure DevOps to interact with the Azure subscription (see [docs](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml#azure-resource-manager-service-connection) for more details)
    - Should be configured prior to the build pipeline being executed
* `containerRegistry`
    - Container registry in which the image for the node being released is found
    - Each environment has a default container registry to which node images get pushed
* `keyVaultName`
    - The name of the key vault from which to download the secrets required for the testing stage of the pipeline
    - A breakdown of the secrets required for the pipeline can be viewed [here](Key%20Vault%20Secrets.md)
* `keyVaultRgName`
    - Name of the resource group in which the key vault is provisioned
* `workingDirectory`
    - Directory in which to execute the pipeline
    - Path to the enrich node directory
* `nodeDisplayName`
    - Display name to use for node
* `meshnodeName`
    - Name to assign to the node
* `snowflakeRole`
    - Role to use for pushing enrich node data to Snowflake
* `developmentDeployment`
    - Flag for whether or not it's a development release
* `terraformConfigResourceGroup`
    - Used for remote storage of Terraform state
    - Name of the resource group in which the Azure storage account used for remote storage is found
* `terraformConfigStorageAccount`
    - Used for remote storage of Terraform state
    - Name of the account used for remote storage
* `terraformConfigContainerName`
    - Used for remote storage of Terraform state
    - Name of the container within the storage account used for remote storage
* `terraformConfigKey`
    - Used for remote storage of Terraform state
    - Key to use for Terraform state file
* `deploymentEnvironment`
    - Environment into which the node is deployed
    - Valid values: `poc1`, `demo`, `development`, `sit`, `production`
