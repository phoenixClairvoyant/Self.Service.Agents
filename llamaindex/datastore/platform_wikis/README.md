## Overview
This repo contains guides that detail the build and deployment processes for various aspects of the CORE Platform

## Table of Contents
* Provision
    * [Base Environment Provisioning - V1](./provision/base_environment/v1/Provision%20Environment.md)
    * [Base Environment Provisioning - V2](./provision/base_environment/v2/Provision%20Environment.md)
    * [Azure DevOps Service Connection Configuration](./provision/base_environment/Service%20Connection%20Configuration.md)
* Ingest
    * Build
        * [DBT Ingestion Node](./ingest/build/Create%20DBT%20Ingestion%20Node%20Build%20Pipeline.md)
        * [SnowSQL CLI Ingestion Node](./ingest/build/Create%20SnowSQL%20CLI%20Ingestion%20Node%20Build%20Pipeline.md)
    * Release
        * [DBT Ingestion Node](./ingest/release/Create%20DBT%20Ingestion%20Node%20Release%20Pipeline.md)
        * [SnowSQL CLI Ingestion Node](./ingest/release/Create%20SnowSQL%20CLI%20Ingestion%20Node%20Release%20Pipeline.md)
* Enrich
    * [Build Pipeline](./enrich/build/Create%20Enrichment%20Node%20Build%20Pipeline.md)
    * [Release Pipeline](./enrich/release/Create%20Enrichment%20Node%20Release%20Pipeline.md)
* Serve
    * React Frontend
        * [Testing Pipeline](./serve/react-frontend/Create%20React%20Frontend%20Testing%20Pipeline.md)
        * [Build and Release Pipeline](./serve/react-frontend/Create%20React%20Build%20And%20Release%20Pipeline.md)
    * PostgREST API
        * [Configuration Pipeline](./serve/postgrest-api/Create%20PostgREST%20API%20Configuration%20Pipeline.md)

## Architecture Descision Records
This repo also curretly house [environment-scoped ADRs](./docs/architectural_decision_records/ADR.md) that apply throughout the cloud environment.

## Networking Notes
This repo also curretly house [Networking Notes](./docs/azure/networking_notes.md) which is a set of notes on Azure networking concepts relevant to Core.

## Notes on Azure Databricks Unity Catalog
This repo also curretly house [Unity Catalog notes](./docs/databricks/unity_catalog.md) which is a set of notes on Azure Databricks Unity Catalog.

## Decision Hypothesis Catalog : Data Modelling Framework
This repo also curretly house the [Decision Hypothesis Catalog: Data Modelling Framework](./docs/decision_hypothesis_catalog/data_modelling/data_modelling_for_enabling_decisions.html) which might assist your thinking when thinking about data management concerns.

