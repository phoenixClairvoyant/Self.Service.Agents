---
id: ADR-003
title: Data Mesh as Overall Architecture
date: 2022/06/21 
status: Accepted
---

# Context

The industry trend and our own gained experience now agree that the traditional centralised, highly coupled approach for developing data-intensive solutions does not scale.
We require an architectural and sosio-technical approach that would promote non-blocking, distributed, loosly coupled, domain-scoped , data-as-a-product approach.

[Data Mesh Architecture](https://www.datamesh-architecture.com/),
first proposed by Zamak Dehghani  ([Data Mesh | Thoughtworks](https://www.thoughtworks.com/what-we-do/data-and-ai/data-mesh#vault)) 
in 2019, acknowledges the industry need for a micro services inspired move towards decentralisation of the data monolith.

# Decision

Adopt a 
[Data Mesh Architecture](https://www.datamesh-architecture.com/)
when developing tools, ways of working and L1 through L3 components.
For reference:

* L0  refers to the public cloud
* L1 refers to PaaS and SaaS bought or built on L0, where no specific business domain knowledge yet exists
* L2 refers to business domain specific knowledge built or bought using L2.
* L3 refers to L2 components offered as SaaS.

# Consequences

* Adopting Data Mesh, being a sosio-technical approach first and foremost demands a holistic approach that is more than merely a single technology stack choice.
* Awareness, training, tooling, reference implementations and data mesh enabling technology stacks are some of the challenges to consider.
* Modularisation at the domain level brings the responsibility of  data quality closer to the domain knowledge holders.
* It is out of scope for this ADR to list all the thuroughly   documented consequences of adopting a data mesh architecture. The reader is encouraged to research data mesh online.
* [Data Mesh, Now](https://www.youtube.com/watch?v=VKDMz8op3VM)
* Data mesh, being a young data architecture,  lacks a mature ecosystem and community.

