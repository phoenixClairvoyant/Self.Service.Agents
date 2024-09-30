---
id: ADR-005
title: Linting
date: 2022/06/21 
status: Accepted
---

# Context

Linters enhance code quality because:
1. Users do not have to concern themselves with code formatting as it is performed automatically
2. Code is standardised across all packages
3. Improve code quality by catching errors and removing code smells such as unneeded imports
4. Code diffs in pull requests will not contain code formatting changes or
   certain bugs, allowing the reviewer to focus on the content
5. The resulting code is simpler to read and understand and therefore easier to
   extend and maintain

# Decision

The repository adopts the use of several linters as defined in `setup.cfg` and
`.pre-commit-config.yaml`.

# Consequences

Al CI pipelines will apply the linters. Users are additionally advised to use
[pre-commit](https://pre-commit.com/) to apply the linters before pushing to
the origin repository.
