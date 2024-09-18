---
id: ADR-004
title: Use cloud vendor-specific services whenever possible
date: 2022/06/21 
status: Accepted
---

# Context

In building data-intensive products, the economics, reliability, security, scalability of cloud services over self hosted, self managed solutions is very attractive.
In addition to these real factors, we have also observed a strong, not necessarily empirically founded,  preference  among customers for cloud vendor specific solutions.
This, in no small way, generates a tension between our ambition to build in a cloud agnostic manner.

# Decision

We strive hard to use cloud vendor-specific services whenever possible.

### Consequences

* Technology choice is limited to what the cloud vendor has to offer, which might not always be the best of breed.
* Major code investment in a cloud vendor-specific technology can be hard and costly to port to another cloud vendor.
* Using cloud vendor-specific technologies and approaches are well supported and generally easier to acquire additional talent for.
