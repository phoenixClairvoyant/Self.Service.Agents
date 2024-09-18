# Environment
rg_location            = "West Europe"
location_shorthand     = "euw"
deployment_environment = "poc"
team_name              = "wwtw"
use_case               = "base"

# Some default vars omitted
postgresql_flexible_server_storage_mb = 131072

# Network
virtual_network_cidr_block = "10.0.0.0/16"
subnet_cidr_block          = "10.0.2.0/24"

# Key vault
service_principal_name = "terraform-service-principal"

# IAM
reader_groups      = ["CORE Team"]
contributor_groups = ["CORE Team"]
