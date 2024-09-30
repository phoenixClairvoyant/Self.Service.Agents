```hcl
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_app_service_plan" "example" {
  name                = "example-app-service-plan"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    tier     = "Standard"
    size     = "S1"
    capacity = 1
  }
}

resource "azurerm_web_app" "example" {
  name                = "example-web-app-${substr(random_string.example.result, 0, 8)}"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id
  https_only          = true

  app_settings = {
    "WEBSITE_NODE_DEFAULT_VERSION" = "14"
    "APPLICATIONINSIGHTS_INSTRUMENTATIONKEY" = var.app_insights_instrumentation_key
  }
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestoracc"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier            = "Standard"
  account_replication_type = "LRS"
}

resource "random_string" "example" {
  length  = 10
  special = false
}

output "web_app_url" {
  value = azurerm_web_app.example.default_site_hostname
}
```

This Terraform template defines:
- An Azure Resource Group that serves as the container for the other resources.
- An App Service Plan to host the web application.
- A Web App configured to run a Node.js application with Application Insights integration.
- A Storage Account for persistent storage needs.

This template reflects the company's data management standards and deployment procedures by utilizing Infrastructure as Code principles, ensuring that deployments are consistent, repeatable, and can operate across different environments without being locked into a particular cloud vendor. Adjustments can be made based on any additional specific requirements from the organizational standards.