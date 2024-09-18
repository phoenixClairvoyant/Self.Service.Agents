### Instructions
1. Copy the [`frontend-app-service.tfvars` example file](https://dev.azure.com/exploreai/CORE.Utilities/_git/Platform.PipelineExamples?path=/provision/variable-files/frontend-app-service.tfvars) locally and prefix the name of the file with the deployment environment type
2. Update the local `.tfvars` variable file with the relevant values (ask an admin to provide sensitive Azure-related values)
3. Navigate to the `Library` tab in the Azure DevOps project and click `Secure Files`
4. Upload the locally created variable file
5. Execute the pipeline manually. You will be prompted to provide the following parameters (*NB* - values that includes spaces are invalid and will lead to pipeline failures):
    <br/> - `Deployment Environment` -> the environment in which the DB is hosted (`development`, `prod`, etc.)
    <br/> - `Team Name` -> Team for whom the app service is being provisioned
    <br/> - `Use Case` -> Use case for which the app service is being provisioned
    <br/> - `App Name` -> the name of the app to be created

    