# Environment
rg_location            = "West Europe"
location_shorthand     = "euw"
deployment_environment = "poc"
team_name              = "wwtw"
use_case               = "base"

rg_name                      = "euw-wwt-bas-poc-rg"
log_analytics_workspace_name = "euw-wwt-bas-poc-log"

# IAM
reader_groups      = ["CORE Team"]
contributor_groups = ["CORE Team"]

# Environment
key_vault_name    = "euw-wwt-bas-poc-kv"
key_vault_rg_name = "euw-wwt-bas-poc-rg"

# App service config
app_service_name = "fastapi"
port             = 80

acr_name     = "euwwwtbaspoccr"
docker_tag   = "latest"
docker_image = "euwwwtbaspoccr.azurecr.io/water_quality_tool_backend-fastapi"

postgresql_flexible_server_name = "euw-wwt-bas-poc-psql"
postgresql_db_name              = "wwtw"
