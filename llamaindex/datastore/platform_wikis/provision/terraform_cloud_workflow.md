# Terraform Cloud workflow

## Terraform Cloud CLI workflow

1. Clone [`Platform.Iac`](https://dev.azure.com/exploreai/CORE.Platform/_git/Platform.Iac) repository.
2. `cd` into the correct terraform script directory for the resources you want to provision.
3. Initialise the project with `terraform init`.
4. If required, create a new workspace for the project with the command `terraform workspace new <workspace-name>` or select the existing workspace with `terraform workspace select <workspace-name>`.
5. On the [EXPLORE-CORE terraform Cloud](https://app.terraform.io/app/EXPLORE-CORE/workspaces) page, go to the workspace and apply the variable set that exists for the target subscription.
	- Navigate on the sidebar to the variables page, scroll down to variable sets and apply a variable set. 
6. Populate the required `.tfvars` file according to the `variables.tf` file (soon to have automatically generated docs in markdown format).
	- We dont commit variables files to version control because they may in general contain secrets. 
	- You need to manually create a variable file and make `terraform plan` or `terraform apply` aware of the file with the `-var-file` option.
7. Run a plan with `terraform plan -var-file=<path_to_tfvars_file>`.
8. If everything is as expected, run an apply with `terraform apply -var-file=<path_to_tfvars_file>`.
	- Everything is as expected if Terraform says it will be creating all the resources that you want it to create, and it is not modifying something it shouldn't be modifying.

## Example `.tfvars` files

Some examples are stored in the [example_tfvars/](./example_tfvars/) directory. Note that values that have sane defaults are not listed at present. See the project `variables.tf` file for further information.

## Terraform workspace tags

We make use of terraform workspace tags are used to identify workspaces that belong to a specific project directory:

- `Platform.Iac/terraform/environment`: `environment` tag
- `Platform.Iac/terraform/fastapi-app-service/`: `fastapi-app-service` tag
- `Platform.Iac/terraform/frontend-app-service/`: `frontend-app-service` tag

## Credentials variable set naming

The subscription credentials contain 4 variables that configure the deployment to target a subscription and service principal within an Azure tenant. These are:
- `tenant_id`: ID of the Azure tenant
- `subscription_id`: ID of the subscription within the Azure tenant
- `client_id`: ID of the service principal which is configured for the target subscription
- `client_secret`: Authentication secret of the service principal

Subscription credentials variable sets are named according to the subscription they belong to

```
[cloud]-[tenant]-[subscription]-ProviderCredentials
```
E.g. for an Azure tenant called, `EAI`, subscription `ProdSimulation` the provider credentials are called:
```
Azure-EAI-ProdSimulation-ProviderCredentials
```

## The use of modules in workspaces

As per [ADR-020](../docs/architectural_decision_records/ADR-020.md), we use a module driven approach where possible. See the ADR for details around the development of modules, naming, tooling and usage.

Published module repositories are stored in the [CORE.Platform devops project](https://dev.azure.com/exploreai/CORE.Platform/_settings/repositories) and are named with the prefix `terraform-`.

## Expected structure of self-service functionality

I see the self-service mechanism as following the above process using the API with a few small changes to make our lives a little better. This mechanism will be contained in an ADO pipeline with sane defaults that SATs can use to deploy or update what they require.

THe process should look like:
1. User select options that form basis of variable file, excluding the subscription variable set contents.
2. User selects target subscription from list.
3. Pipeline clones and cds to correct project code in `Platform.Iac`.
4. Pipeline configures the workspace.
  a. Pipeline checks if the terraform workspace exists matching pipeline input conifguration.
  b. If workspace exists, the workspace is selected. If not, the workspace is created and the subscription variable set is assigned to the new workspace.
5. A terraform apply is run - we can use the same workflow as before where we have a flag for allowing destructive changes or not to block or allow changes where certain resources are destroyed or modified in place.
6. Variables selected in pipelines are uploaded to the terraform workspace so that they are persisted on tf cloud's webpage.
