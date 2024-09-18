## Overview
IAM for CORE environments is managed using [built-in Azure roles](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles). Role assignments are separated into 2 groups, with one assigning read permissions that allow users to view resources in an environment, and a second group that allows users (admins) to modify resources. This is necessary for certain actions such as IP whitelisting on DBs, setting up access policies on key vaults, etc. No roles are assigned that allow users to manage RBAC within an environment.

## How It Works
The [infrastructure repo](https://dev.azure.com/exploreai/CORE.Platform/_git/Platform.Infrastructure) contains a set of scripts for assigning the [IAM roles](https://dev.azure.com/exploreai/CORE.Platform/_git/Platform.Infrastructure?path=/IAM). The [`local.tf` file](https://dev.azure.com/exploreai/CORE.Platform/_git/Platform.Infrastructure?path=/IAM/local.tf) contains a mapping called `teams` that's used to define the members that make up different stream aligned teams. At the top level, the mapping contains nested mappings for each client (e.g. `severntrent`), which then contains another nested mapping that specifies the different teams/use cases for each client. This mapping has 2 keys, `users` and `admins`, the value for each of which is a list of the emails for the users that belong to said group for each team. When the pipeline is executed, the user emails are used to fetch data about each user from within the Azure Active Directory tenant, which then allows for roles to be assigned to each individual user

## Roles
The [Reader](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader) role is assigned to standard users and the [Contributor](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor) role is assigned to admin users for the following resources in an environment:  
- Resource Group 
- Virtual Machines 
- Key Vault
- Database Server
- Databricks workspace
- Azure Container Registry
- Storage Account

## Common Errors
- `Error: authorization.RoleAssignmentsClient#Create: Failure responding to request: StatusCode=409`  
    + Occurs when attempting to assign a role to a user when said role has already been assigned outside of the pipelie (i.e. via the Azure portal or CLI)
    + Resolution: Remove role assignment via the portal and execute pipeline again