## Common Variables
+ `subscription_id` 
    - ID of the Azure subscription in which the resources are provisioned. Used to provide secure access to Azure estate.
+ `client_id` 
    - ID of the client credentials for the service principal used for Terraform. Used to provide secure access to Azure estate.
+ `client_secret` 
    - Secret value generated as part of the client credentials for the service principal used for Terraform . Used to provide secure access to Azure estate
+ `tenant_id` 
    - ID of the Azure AD tenant used for service principal authentication. Used to provide secure access to Azure estate
+ `deployment_environment`
    - Label for the environment being provisioned. 
    - Accepted values: `demo`, `poc1`,`development`, `sit`, `production`
+ `target_environment`
    - Value used for tagging provisioned resources
    - Identical to resource group name 
+ `rg_name`
    - Name of the resource group to be provisioned. The resource group gets provisioned in the first stage of the pipeline and is referenced by all other resources. 
    - Naming convention: `<team_name>.<use_case>.<deployment_environment>`
    - Name should be title-cased
+ `rg_location`
    - Location of the resource group to be provisioned
    - The resource group gets provisioned in the first stage of the pipeline and is referenced by all other resources.
    - You can view a list of Azure regions [here](https://azure.microsoft.com/en-gb/global-infrastructure/geographies/#geographies)
+ `key_vault_name`
    - Name of the key vault to be provisioned and used within an environment
    - Provisioned in the third stage of the pipeline
    - Is referenced by other resources when uploading new secrets to the key vault or accessing existing secrets
    - Naming convention: `<location_shorthand>-<team_name>-<use_case>-<deployment_environment>`, e.g. `euw-core-internal-demo`
    - *NB*: Key vault names are limited to 24 characters long. It may be necessary to veer from the convention/protract the key vault name to abide by the character limit
+ `key_vault_rg_name`
    - Resource group in which the key vault is provisioned
    - Should match the `rg_name`
+ `environment_name`
    - Used to label resources
    - Should match the `<team_name>` 

## Blob Storage
+ `account_name`
    - Name of the storage account to be provisioned
    - Naming convention: `<team_name><use_case><deployment_environment>`, e.g. `coreinternaldemo`
    - *NB*: Storage account names are limited to 24 characters long. It may be necessary to veer from the convention/protract the key vault name to abide by the character limit
+ `container_name`
    - Name of the storage container to be provisioned within the storage account
    - Naming convention: `<team_name>-<use_case>-<deployment_environment>-container`, e.g. `core-internal-sit-container`

## Compute
+ `workspace_users`
    - A mapping of the users to assign to the workspace, where the key is the user's email and the value is the user's name

## Container Registry
+ `registry_name`
    - Name of the container registry to be created
    - Naming convention: `<location_shorthand><team_name><use_case><deployment_environment>`, e.g. `euwcoreinternaldemo`

## Database
+ `db_admin_password`
    - Secure password to be used for admin authentication to the DB
    - Default admin username is `psqladmin`

## Databricks Groups
+ `workspace_users`
    - A mapping of the users to assign to the workspace, where the key is the user's email and the value is the user's name

## IAM
+ `deployment_stage`
    - Same as `deployment_environment` 
+ `mesh_vm_name`
    - Name assigned to the virtual machine provisioned as part of the base environment
    - Naming convention: `<location_shorthand>-<team_name>-<use_case>-<deployment_environment>-mesh-vm`
+ `db_name`
    - Name assigned to the virtual machine provisioned as part of the base environment
    - Naming convention: `<location_shorthand>-<team_name>-<use_case>-<deployment_environment>-postgresql-flexible-server`
+ `databricks_workspace_name`
    - Name assigned to the virtual machine provisioned as part of the base environment
    - Naming convention: `<location_shorthand>-<team_name>-<use_case>-<deployment_environment>-databricks-workspace`
+ `acr_name`
    - Name assigned to the virtual machine provisioned as part of the base environment
    - Naming convention: `<location_shorthand><team_name><use_case><deployment_environment>`
+ `storage_account_name`
    - Name assigned to the virtual machine provisioned as part of the base environment
    - Naming convention:  `<team_name><use_case><deployment_environment>`

## Key Vault
+ `user_ids`
    - A list of object IDs for users to be assigned read permissions on the secrets in the key vault
    - The object IDs can be obtained via the Azure portal or Azure CLI
+ `admin_ids`
    - A list of object IDs for users to be assigned read, write and delete permissions on the secrets in the key vault
    - The object IDs can be obtained via the Azure portal or Azure CLI
+ `pipeline_object_id`
    - The object ID of the service agent for an Azure DevOps project
    - Used to provide access to key vaults from DevOps pipelines within a project
    - Can be obtained via the Azure DevOps portal

## Virtual Network
+ `virtual_network_cidr_block`
    - The CIDR block to be assigned to the virtual network
+ `subnet_cidr_block`
    - The CIDR block to be assigned to the subnet
