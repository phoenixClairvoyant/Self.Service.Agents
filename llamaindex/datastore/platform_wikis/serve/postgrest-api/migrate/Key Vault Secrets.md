## Key Vault Secrets
Azure Key Vault is used to store and access sensitive variables (e.g. credentials, access tokens) in various parts of the CORE Platform, including pipelines. The following is a breakdown of the secrets that are required for setting up an enrich node build pipeline.

## Environment Secrets
* The current secrets are required for the pipeline and have to exist in the key vault for a given environment: 
    - `escaped-db-admin-username`
        - The URL-escaped username of the admin account for the PostgreSQL database server used by the API
        - Has to be added manually after the base environment is provisioned
    - `escaped-db-admin-password`
        - The URL-escaped password of the admin account for the PostgreSQL database server used by the API
        - Has to be added manually after the base environment is provisioned
    - `db-server-host`
        - The host of the PostgreSQL database server used by the API
        - Has to be added manually after the base environment is provisioned