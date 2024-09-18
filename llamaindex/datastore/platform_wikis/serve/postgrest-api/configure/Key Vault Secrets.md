## Key Vault Secrets
Azure Key Vault is used to store and access sensitive variables (e.g. credentials, access tokens) in various parts of the CORE Platform, including pipelines. The following is a breakdown of the secrets that are required for setting up an enrich node build pipeline.

## Environment Secrets
* The current secrets are required for the pipeline and have to exist in the key vault for a given environment: 
    - `db-admin-username`
        - Username of the admin account for the PostgreSQL database server used by the API
        - Has to be added manually after the base environment is provisioned
    - `db-admin-password`
        - Password of the admin account for the PostgreSQL database server used by the API
        - Is populated automatically as part of the base environment provisioning
    - `db-authenticator-role-password`
        - Password of the `authenticator` account for the PostgreSQL database server used by the API
        - Has to be added manually after the base environment is provisioned
    - `api-jwt-secret`
        - The secret value used by the PostgREST API for generating JWT tokens
        - Has to be added manually after the base environment is provisioned
    - `api-username`
        - Username of the superuser account for the PostgREST API
        - Has to be added manually after the base environment is provisioned
    - `api-password`
        - Password of the superuser account for the PostgREST API
        - Has to be added manually after the base environment is provisioned
    - `api-webuser-username`
        - Username of the `webuser` account for the PostgREST API
        - Has to be added manually after the base environment is provisioned
    - `api-webuser-password`
        - Password of the `webuser` account for the PostgREST API
        - Has to be added manually after the base environment is provisioned