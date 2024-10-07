### Task-Specific Startup Template for Azure Resource Group Provisioning

This startup template includes all necessary components for provisioning an Azure Resource Group using Terraform, adhering to organizational standards.

#### Directory Structure
```
/terraform
  ├── modules
  │   └── resource_group
  │       └── main.tf
  ├── main.tf
  ├── variables.tf
  └── outputs.tf
```

---

#### 1. `modules/resource_group/main.tf`
```hcl
resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location

  tags = {
    Environment = var.environment
    Team        = var.team
    Project     = var.project
  }
}
```

#### 2. `variables.tf`
```hcl
variable "resource_group_name" {
  description = "The name of the Resource Group"
  type        = string
}

variable "location" {
  description = "The Azure Region where the Resource Group will be created"
  type        = string
}

variable "environment" {
  description = "The environment (e.g., dev, prod)"
  type        = string
}

variable "team" {
  description = "The team responsible for the Resource Group"
  type        = string
}

variable "project" {
  description = "The project associated with the Resource Group"
  type        = string
}
```

#### 3. `outputs.tf`
```hcl
output "resource_group_id" {
  description = "The ID of the Resource Group"
  value       = azurerm_resource_group.main.id
}
```

### Conclusion
By following this organized structure and utilizing the provided Terraform configuration files, the provisioning of an Azure Resource Group will comply with organizational standards and best practices for infrastructure-as-code.