---
id: ADR-002
title: Build as cloud-native and cloud-agnostic as possible with IaC
date: 2021/11/01 
status: Accepted
---

# Context

* We are unsure which of the cloud vendors our first customer will mandate that we build on.
* We would like to make it as painless as possible to switch between the three major cloud vendors: AWS, Azure, GCP.
* IaC or infrastructure as code has become mainstream and best practice.

# Decision

* We choose to prefer technologies and architectures not bound to a single cloud vendor, and to build solutions using IaC where possible.
* When we build, we strive to build in a cloud-native way, which means we do not simply port to the cloud but reimagine for the cloud.

# Consequences

* IaC is harder and more time consuming upfront than simply using the cloud vendor's Web UI portal.
* Building in a cloud-agnostic manner is harder than targetting one specific cloud vendor.
* Building with IaC and as cloud-agnostic as possible forces more modular and better overall architecture.
* Building cloud-native requires new know-how and skills to acquire.

