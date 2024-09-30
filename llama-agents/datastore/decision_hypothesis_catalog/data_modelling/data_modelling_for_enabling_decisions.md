# Data Modelling For Enabling Decisions

Our decisions rely on, and ultimately produce data, but what data?

 - We have a need to define and communicate a perspective on decision enabling data.
 - When we define and communicate a perspective on the required and produced decision-related data, we say that we model data.
 - We avoid "boiling the ocean" by restricting the scope and detail of our data model.
 - Our model should be scoped and detailed so that it enables reasoning about the domain, and allows technical implementation, but no more than that.

Different people or personas need to comprehend our model, at varying levels of detail.
We can say that we need a multi-modal model.

It is useful for us to distinguish between various complementary, sometimes successive types of data models:
 
* [**Anecdotal**](anecdotal_data_model.md) - consisting of free-form story-like description of the data in the domain; 
* [**Conceptual**](conceptual_data_model.md) - consisting of entities, attributes, keys and relationships in the decision domain;
* [**Relativistic**](relativistic_data_model.md) - consisting of temporal, spacial, granularity and the *5 V's* of big data;
* [**Governance**](governance_data_model.md) - comprising ownership, management, control, privacy, and security aspects;
* [**Economic**](economic_data_model.md) - consisting of value, cost and mathematical relations;
* **Logical** -  consisting of a storage agnostic translation of the conceptual model, and
* **Physical** - consisting of the logical model implemented for a particular storage technology. 

For enabling decisions, we focus on the anecdotal, conceptual and relativistic models.

## Progression, or lack there of in the various models

Although there is a naturaal progression from anecdotal -> conceptual -> relativistic, this does by no means imply that we have to first fully complete one model before starting on the next.
It is perfectly normal - and even encouraged - to partially complete the anecdotal model while starting on the conceptual, and the same applies for the conceptual and relativistic.
When capturing the data requirements in terms of the data model, we will often have to flip between the various perspectives.
Having said that, there are aspects of each model that informs the next.
The key takeaway is that we need not imagine that we have to fully complete one model before starting on the next one, but instead evolve the entire system iteratively.

## Personas
We identify the following "personas" as the intended audience and authors of the various models:

* Customer-capability persona comprised of program leads and business analysts;
* Technical-capability persona comprising of technical leads, data and software engineers, data scientists

## Notes:

* Try and add  more questions to each of the models. Questions can assist people in getting to the meat of what matters.
