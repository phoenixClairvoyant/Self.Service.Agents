---
id: ADR-001
title: Architectural decision records
date: 2022/06/21 
status: Accepted
---

# Context

We require a mechanism to document important architectural decisions in a
systematic manner for contributors and interested parties to understand the current state of the
project.

# Decision

Each architectural decision record will be a markdown file containing a
[yaml front matter](https://assemble.io/docs/YAML-front-matter.html)
block containing:
1. `id`: enumerated id number of the form `ARD-x`
2. `title`: title of the ADR
3. `date`: date when the ADR was posed
4. `status`: one of Proposed, Accepted, Deprecated
5. `deprecated by`: optional field if status is `deprecated` containing
    value of the deprecating ADR id.

In following, there will be H1 headings for `Context`, `Decision` and
`consequences`.

The filename stem will be the id.

# Consequences

All future ADRs will be  captured in this format within the directory:
`docs/architectural_design_records/`.
