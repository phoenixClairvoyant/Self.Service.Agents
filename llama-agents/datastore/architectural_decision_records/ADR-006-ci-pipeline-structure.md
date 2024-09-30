---
id: ADR-006
title: CI pipeline template
date: 2022/06/21 
status: Accepted
---

# Context

A byproduct of monorepos is increased complexity of CI pipelines given that
multiple projects need to be built and maintained independently of oneanother
from a single codebase.

This ADR specifies a standard CI pipeline template that can be applied to all projects
to standardise build processes across projects, thus reducing repo complexity
and heterogeneity.

# Decision

The CI pipelines follow the following steps for every package in the monorepo
after a pull request has been opened, for each commit:

1. Run linters
2. Compile code (if required)
3. Run tests
4. Build package(s)
5. If docker images are used:
    1. Build, push docker image(s) tagged with latest commit hash
    2. Tag image(s) with latest commit hash
    3. Push image(s) to appropriate repository
6. If merge commit:
    1. Push python packages to PyPI
    2. if docker images are used:
        1. Tag image(s) with "latest" tag
        2. Push docker image(s)

This automates the development lifecycle by:
1. Ensuring that PRs that have successfully passed the pipeline are correctly
   linted and tested
2. Intermediate docker images are built and uploaded to the requisite repository
   for testing puposes before completion of the PR
3. Code is always deployed when a PR is merged, thus sticking closely to trunk
   development practices

# Consequences

All projects' CI pipelines will conform to this specification.
