# Active Component Discussion for the Sketch Component Playbook

Thanks, everyone again for your active participation in the meeting! Here are some of the things we discussed: 

## Principals
Could we agree on some of these principals?

* This is primarily a software engineering and architecture problem: on the "building platform and component templates" level AND on the "making use of the component templates" to bring to life new domain value.
* We cannot succeed without clear and complete requirements and drivers, and alignment on them.
* We use the best technology, technique or methadology for the task at hand, not the most familiar and comfortable by default.
* We trust the various experts to define "the best".
* We require that the definition of "the best" be justified by the expert's experience, reasonable logical arguments and reference to current industry trends.
* We agree that the definition of "the best"  realistically should satisfy requirements and various drivers.
* We accept that it is far more preferrable to build correct from the start, bringing along domain expertise and artifacts than to try and panelbeat existing work into submission.
* We accept that "the best" might bring with it a learning cost, which we embrace.
* We admit that we should draw and learn from the software engineering  collective wisdom in academia and industry which has been developing  since the 1960's and make sure we don't follow our own ideas just because they sound nice.
* It is not business as usual as before, but we are in a better position with Sand, so we can do things with a more long-term vision in mind.
* Platform is the ecosystem that tests, builds, deploys, runs, host a repository of components, provide a dev env for component development.

## Open questions about component work:
Thinking influenced by experience and [Component-Based Software Engineering Methods and MetricsBy Umesh Kumar Tiwari, Santosh Kumar, Copyright 2021](https://www.routledge.com/Component-Based-Software-Engineering-Methods-and-Metrics/Tiwari-Kumar/p/book/9780367354886).
Heareafter referred to as CBSE book.

### 1.  What is a component, and are there different types?
We know this is hard to define because a component can be so many things.
CBSE  gives general and then SE industry leaders definitions of component and then states this:

From an analysis of these prominent and diverse definitions, one can deduce that they all contain a number of universal points. In the context of this work and in the light of these universal directives, we can identify a general definition of components as follows:
*  A component is an identifiable, functionally reusable unit (element/part/piece/package) of a larger software system.
* A component is developed independently.
* A component is delivered and deployed in a context-free environment.
* A component interacts with other components through well-defined interfaces to access and to provide services.
* A software component can be a replaceable, modifiable piece of code that can be integrated with other replaceable, modifiable components.

#### Kinds and examples:
* A powerful and working piece of technology like a software system such as a RDBMS (PostgreSQL) for example is a component.
* A complete system that can do metadata management, such as DataHub or Azure Perview is a component.
* A combination of DS algorithms and data structures, packaged up using Core-developed component templates, that say performs building polygon boundary detection / classification is a component.
* A collection of programs that efficiently ingest data landed in a cloud storage bucket into a RDBMS, built using a Core-developed component template is a component.
* A collection of inter-dependant data model declarations, described in SQL, packaged up in a Core-developed component template is a component. 

#### Fundamentally we have these types of components:
* Component off-the-shelf  COTS: buy or built before which we can reuse immediately with the least amount of configuration.
* Adaptable components which we can modify to create new components which we can then use.
* New components we develop from scratch.

### 2. When do we build a component?
Only if in this order of presidence:
0. There is a direct or indirect, justifiable need.
1. We cannot "buy" or reuse one that will satisfy requirements.
2. We cannot configure (without adapting) an existing component, or set of composed components to satisfy the requirements.
3. We cannot adapt and configure an existing component, or set of composed components to satisfy the requirements.

### 3. How are components built? 
In such a way that we optimise for (in this order):
1. Reusability
1. Composability
1. Deployability
1. Discoverability

By being informed by these software engineering paradigms:
* CBSE - component-based software engineering
* AOP/AOSE - aspect-oriented programming and software engineering to better do shared concerns
* CRSE - clean room software engineering with formal verification for selective "components to build components with".

### 4. How do we convert an instance of current IP into a component, and how demanding is the task compared to building one from scratch?
* We should make peace with the fact that "building from scratch" is far cheaper in the long run, always.
	- We are in 2024, have LLM's a plaphora of tools, languages, open source, closed source, smart people, many people!
* We should also acknowledge that "building from scratch" does not mean a reinvention of the true IP,  but just a repackaging of it.
	- Throwing away a solution does not mean we destroy IP if we reeuse the true IP in a new jacket.

The ease to wich current IP can be reused depends on the maturity of the IP:
* Easiest if the builders are still with us and actively working on it.
* Easier if the IP has a way of being automatically tested.

### 5. If the Core builds shared components, what is the nature of these components? 
* They are cognitive load reducers in nature.
	- Cognitive load of building data-intensive applications as components is too high: Core-built component templates and accelerators reduce this.
* They minimise boilerplate that domain component developers have to write.
* They bring into high and sharp focus the essential IP: the "special sauce", the innovation in terms of AI/DS/DE code.
* They allow 90% of a component developer's time to be spent on the domain data model, data science model.

### 6. How do components fit into the broader process and system of value delivery, as enabled by the Core?

### 7. How do we know when we're done building a component?

Developing artefacts: 
 - Component Building Playbook
 - Component Definition of Done (DoD)

# References
* [Component-Based Software Engineering: Methods and Metrics](https://www.routledge.com/Component-Based-Software-Engineering-Methods-and-Metrics/Tiwari-Kumar/p/book/9780367354886)
