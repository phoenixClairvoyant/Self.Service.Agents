# Environment
rg_location            = "West Europe"
location_shorthand     = "euw"
deployment_environment = "poc"
team_name              = "wwtw"
use_case               = "base"

rg_name                      = "euw-wwt-bas-poc-rg"
log_analytics_workspace_name = "euw-wwt-bas-poc-log"

# IAM
reader_groups      = ["CORE Team", "az-we-sw-wwtw-poc-sg"]
contributor_groups = ["CORE Team", "az-we-sw-wwtw-poc-sg"]

#App service config
app_service_name = "app"
app_command_line = "pm2 serve /home/site/wwwroot --no-daemon --spa"
