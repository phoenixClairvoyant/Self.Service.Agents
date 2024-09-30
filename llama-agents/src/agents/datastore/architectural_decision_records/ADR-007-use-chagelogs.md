---
id: ADR-007
title: Use of changelogs
date: 2022/06/22 
status: Accepted
---

# Context

When developing multiple packages, it is important for users see when notable
changes have been made. Since [ADR-4](./ADR-4.md) introduced semantic versioning,
we can can explicitly state which changes were included in each version.

# Decision

Each package in the monorepo will contain a [changelog](https://keepachangelog.com/)
that will document the changes made to the code for each version.

## Keeping a changelog

The following sections outline how changelogs should be updated as discussed in 
[how do I make a good changelog](https://keepachangelog.com/en/1.0.0/#how).

### Changelog guiding Principles

- The latest version comes first.
- Changelogs are for humans, not machines.
- There should be an entry for every single version.
- The same types of changes should be grouped.
- Versions and sections should be linkable.
- The release date of each version is displayed.

### Types of changes

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

# Consequences

Contributors are required to update the changelog when committing to the
package.
