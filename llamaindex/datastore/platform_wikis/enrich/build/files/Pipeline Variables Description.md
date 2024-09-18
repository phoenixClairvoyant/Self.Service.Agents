## Pipeline Variables
* `project-acr-service-endpoint`
    - The service endpoint used by Azure DevOps to interact with the container registry to which the image gets pushed (see [docs](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml#docker-hub-or-others) for more details)
    - Should be configured prior to the build pipeline being executed
    - Is set up as part of the base environment configuration
* `explorecore-acr-service-endpoint`
    - The service endpoint used by Azure DevOps to interact with the CORE Platform container registry that hosts the base images for nodes
    - Should be configured prior to the build pipeline being executed
    - Is set up as part of the base environment configuration
* `arm-service-connection-endpoint`
    - The service endpoint used by Azure DevOps to interact with the Azure subscription (see [docs](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml#azure-resource-manager-service-connection) for more details)
    - Should be configured prior to the build pipeline being executed
    - Is set up as part of the base environment configuration
* ` key-vault-name`
    - The name of the key vault from which to download the secrets required for the testing stage of the pipeline
    - A breakdown of the secrets required for the pipeline can be viewed [here](Key%20Vault%20Secrets.md)
    - The key vault is provisioned as part of the base environment configuration. However, certain values have to be populated manually after provisioning
* `working-directory`
    - Directory in which to execute the pipeline
    - Uses the AZDO built-in `System.DefaultWorkingDirectory` variable which points to the directory the repository is checked out in which the pipeline is being executed
* `meshnode-name`
    - Name of the meshnode
* `project-name`
    - Name assigned to the docker-compose project