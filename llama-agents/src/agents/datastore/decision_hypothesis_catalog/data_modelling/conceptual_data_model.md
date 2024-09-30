# Conceptual Model
In defining the conceptual model we need to consider the following elements, in this order of importance:

1. Entity classes;
1. Relationships between entity classes;
1. Attributes of entity classes and relationships, and
1. Uniquely defining keys of entity classes and relationships.

* Out of these four elements, Entity classes are the most important and should be captured completely.
* This is not to say that relationships, attributes and keys are unimportant, but it is to be expected that these elements will be completed itteratively.
* Similar to the anecdotal model, a partially completed conceptual model could be parked while we move back and forth between the anecdotal and relativistic models.

## Persona audience

* Customer-capability
* Intelligence-capability

## Questions that need answering
To build a conceptual data model, we need answers to the following questions:

1. **Which entity classes are used within the solution:** Identify all the real-world or virtual entities we have to model and in which source data they are found. Some entities might be spread out over multiple sources.
2. **What attributes are associated with each entity class:** for each entity class modelled, identify the set of attributes we have to track changes for.
3. **How is uniqueness defined for an entity class:** Identify the attribute(s) that uniquely define each entity class we will be modelling.
4. **When do attributes of an entity change:** Group attributes into related subsets, taking into account the rate of change such that attributes changing at similar rates are grouped together.
5. **What relationships and events exist between entities:** For all modelled entity classes, identify all the relationships and events involving more than one entity class.
6. **What uniquely defines a relationship:** Identify all attributes associated with the relationship or event that are key in defining it.
7. **What additional attributes are important in relationships:** Make a distinction between those that define the relation and those that represent information that need to be tracked over time.

## Example

### Input
Based on the anecdotal model (or part of it), we derive the conceptual model.

#### Entity classes

* geographic_region
* geographic_area
* hydraulic_system
* flow_metered_zone
* measurement_tag
* service_reservoir

#### Relationships between entity classes

* **network_hierarchy** --> Relating `geographic_region` to `geographic_area` to `hydraulic_system` to `flow_metered_zone`.
* **measurement_tag_measurement_value_link** --> Relating `measurement_tag` to a specific timestamp and measurement value in time.
* **flow_metered_zone_measurement_tag_link** --> Relating `flow_metered_zone_measurement_tag_link` to `measurement_tag`.
* **service_reservoir_hydraulic_system_link** --> Relating `service_reservoir` to `hydraulic_system`.

#### Attributes of entity classes and relationships

* geographic_region
	- code
	- name
	- geography_polygon
* geographic_area
	- code
	- name
	- geography_polygon
* hydraulic_system
	- code
	- name
	- geography_polygon
	- precipitation level
* flow_metered_zone
	- code
	- name
	- geography_polygon
* measurement_tag
	- code
	- measurement_type: pressure, flow, volume, precipitation
	- description
	- engineering_unit
* service_reservoir
	- code
	- name
* network_hierarchy
	- geographic_region
	- geographic_area
	- hydraulic_system
	- flow_metered_zone
* measurement_tag_measurement_value_link  
	- measurement_tag
	- measurement_timestamp
	- measurement_value
* flow_metered_zone_measurement_tag_link
	- flow_metered_zone
	- measurement_tag
	- directionality
* service_reservoir_hydraulic_system_link
	- hydraulic_system
	- service_reservoir
* precipitation_hydraulic_system_link
	- hydraulic_system
	- measurement_tag

#### Uniquely defining keys of entity classes and relationships

* geographic_region
	- code
* geographic_area
	- code
* hydraulic_system
	- code
* flow_metered_zone
	- code
* measurement_tag
	- code
* service_reservoir
	- code
* network_hierarchy
	- geographic_region
	- geographic_area
	- hydraulic_system
	- flow_metered_zone
* measurement_tag_measurement_value_link  
	- measurement_tag
	- measurement_timestamp
	- measurement_value
* flow_metered_zone_measurement_tag_link
	- flow_metered_zone
	- measurement_tag
	- directionality
* service_reservoir_hydraulic_system_link
	- hydraulic_system
	- service_reservoir


### Output

The output data surfaces all of the input data, but adds some additional components, namely, aggregated measurements along the hierarchy levels.


### Glossary

 - The Entity Relationship Data Model: [link](https://opentextbc.ca/dbdesign01/chapter/chapter-8-entity-relationship-model/)
