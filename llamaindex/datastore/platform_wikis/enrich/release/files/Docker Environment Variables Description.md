## Environment Variables
* `TF_VAR_workspace_users` (To Be Removed)
    - Mapping of the users to assign to the Databricks workspace
    - The pipeline currently uses a default value of  `{}`. The workspace users are currently set at a workspace level when the base environment is provisioned.
* `TF_VAR_meshnode_name`
    - Name to assign to the node
    - Maps to the `meshnodeName` variable set in the pipeline
* `CLUSTER_SIZE`
    - The size of the cluster to use for the Databricks jobs instantiated for the node
    - Maps the to `clusterSize` variable selected when the pipeline gets executed
* `DATABRICKS_HOST`
    - The URL for the Databricks workspace in which the job is created
    - Maps to the `databricks-host` secret retrieved from the key vault
* `DATABRICKS_TOKEN`
    - The PAT for the Databricks workspace in which the job is created
    - Maps to the `databricks-token` secret retrieved from the key vault
* `TERRAFORM_CONFIG_RESOURCE_GROUP`
    - Name of the resource group in which the Azure storage account used for remote storage is found 
    - Maps to the `terraformConfigResourceGroup` variable set in the pipeline
* `TERRAFORM_CONFIG_STORAGE_ACCOUNT`
    - Name of the account used for remote storage
    - Maps to the `terraformConfigStorageAccount` variable set in the pipeline
* `TERRAFORM_CONFIG_CONTAINER_NAME`
    - Name of the container within the storage account used for remote storage
    - Maps to the `terraformConfigContainerName` variable set in the pipeline
* `TERRAFORM_CONFIG_CLIENT_ID`
    - The ID of the client secret for the service principal used by Terraform for authentication within Azure 
    - Maps to the `terraform-config-client-id` secret retrieved from the key vault
* `TERRAFORM_CONFIG_CLIENT_SECRET`
    - The value of the client secret for the service principal used by Terraform for authentication within Azure  
    - Maps to the `terraform-config-client-secret` secret retrieved from the key vault
* `TERRAFORM_CONFIG_TENANT_ID`
    - The Azure Active Directory tenant ID used by Terraform for authentication within Azure
    - Maps to the `terraform-config-tenant-id` secret retrieved from the key vault
* `TERRAFORM_CONFIG_SUBSCRIPTION_ID`
    - The Azure subscription ID used by Terraform for authentication within Azure
    - Maps to the `terraform-config-subscription-id` secret retrieved from the key vault
* `SF_VAR_snowflake_account_id`
    - ID for the Snowflake account used by the node
    - Maps to the `snowflake-account-id` secret retrieved from the key vault
* `SF_VAR_snowflake_account_username`
    - Username for the Snowflake account used by the node
    - Maps to the `snowflake-username` secret retrieved from the key vault
* `SF_VAR_snowflake_account_password`
    - Password for the Snowflake account used by the node
    - Maps to the `snowflake-password` secret retrieved from the key vault
* `SF_VAR_snowflake_role`
    - Role to use for pushing enrich node data to Snowflake
    - Maps to the `snowflakeRole` variable set in the pipeline
* `DEVELOPMENT`
    - Flag for whether or not it's a development release
    - Maps to the `developmentDeployment` variable set in the pipeline
* `TF_VAR_cluster_size`
    - The size of the cluster to use for the Databricks jobs instantiated for the node
    - Maps the to `clusterSize` variable selected when the pipeline gets executed
* `TF_VAR_key_vault_name`
    - The name of the key vault from which to download the secrets required for the testing stage of the pipeline
    - Maps the to `keyVaultName` variable selected when the pipeline gets executed
* `TF_VAR_key_vault_rg_name`
    - Name of the resource group in which the key vault is provisioned
    - Maps the to `keyVaultRgName` variable selected when the pipeline gets executed

## Template Values
* `meshnode_name`
    - Name to assign to the node
    - Should be the same as the `meshnodeName` assigned in the pipeline
* `container_registry`
    - Name of the container registry in which the node image is hosted
    - Should be the same as the `containerRegistry` assigned in the pipeline