## Key Vault Secrets
Azure Key Vault is used to store and access sensitive variables (e.g. credentials, access tokens) in various parts of the CORE Platform, including pipelines. The following is a breakdown of the secrets that are required for setting up an enrich node build pipeline.

## Environment Secrets
* The current secrets are required for the pipeline and have to exist in the key vault for a given environment: 
    - `databricks-host` 
        - URL for the databricks workspace in which the cluster used for testing exists
        - Has to be added manually after the base environment is provisioned
    - `databricks-token`
        - PAT used to authentication in the databricks workspace
        - Has to be added manually after the base environment is provisioned
    - `snowflake-username`
        - Username for the Snowflake account used by pipeline
        - Has to be added manually after the base environment is provisioned
    - `snowflake-password`
        - Password for the Snowflake account used by pipeline
        - Has to be added manually after the base environment is provisioned
    - `snowflake-account-id`
        - ID for the Snowflake account used by pipeline
        - Has to be added manually after the base environment is provisioned
    - `db-admin-username`
        - Username of the admin account for the PostgreSQL database server used by the node
        - Has to be added manually after the base environment is provisioned
    - `db-admin-password`
        - Password of the admin account for the PostgreSQL database server used by the node
        - Is populated automatically as part of the base environment provisioning