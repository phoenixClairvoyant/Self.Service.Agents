## Pipeline Variables
* `armServiceConnectionEndpoint`
    - The service endpoint used by Azure DevOps to interact with the Azure subscription (see [docs](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml#azure-resource-manager-service-connection) for more details)
    - Should be configured prior to the build pipeline being executed
    - Is set up as part of the base environment configuration
* `rgName`
    - Name of the Azure resource group in which the DB server that hosts the API database is found
* `serverName`
    - Name of the Azure PostgreSQL server that hosts the API database
* `keyVaultName`
    - The name of the key vault from which to download the secrets required for the testing stage of the pipeline
    - A breakdown of the secrets required for the pipeline can be viewed [here](Key%20Vault%20Secrets.md)
* `containerRegistryServiceEndpoint`
    - The service endpoint used by Azure DevOps to interact with the container registry for docker-related tasks 
* `apiDirectory`
    - Directory in which the API code is found
* `projectName`
    - Name assigned to the docker-compose project
* `dbName`
    - Name of the API database
* `dbServerHost`
    - FQDN of the database server