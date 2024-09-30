# Anecdotal model

- The anecdotal model of the data is expressed in a detailed, free-form textual description of the data, ideally resembling a story.

 The sentances of the textual description emerge out of the answers to a set of questions about the data.
- The questions to be answered should be informed by the Basic Five Elements of a story: plot, actors, resolution, conflict and setting.
- While formulating the Basic Five Elements of the data story, the Five W's of Data can be a helpful thinking tool.
- The Five W's of Data are:  Who, What, When, Where and Why.
- The anecdotal model is not meant to be precise and may rely on a lot of assumptions.
- It is worth while captureing any assumptions made.
- The anecdotal model need not be exaustive, but it needs to have enough detail so that it can power the formation of the remaining models.
- It is perfectly acceptable to park a partially completed anecdotal model, and do some work on the conceptual and relativistic models, before returning to continue with the anecdotal model.
	- This is encouraged to save on context switching while dealing with a particular set of entities.

## Persona audience

* customer-capability

## Questions that need answering

### Story of the data
Everything starts with a story, and a decision enabling system should be no exception.

The **data story**, like any real-world story consist of five elements: the actors/characters, the setting, the plot, the conflict and the resolution.

We can use the acronym PARCS: Plot, Actors, Resolution, Conflict and Setting, although this does not imply the best ordering.

* **Actors** : which real-world or virtual actors are involved?
* **Plot** : what is the progression of data over time and space?
* **Setting** as a description of the domain and the various "worlds" the actors inhabit.
* **Conflict** that there currently or potentially can exist related to the data.
* **Resolution**, present or future progression that resolves the conflict.

PARCS is merely a guide, and the data story may comprise of more or less, or even additional components.
Consult the example below for an illustration of how PARCS can be used.

### Five W's of data
The **Five W's of data** may assist us in the formation of the anecdotal model.

* **What** data do we require?
* **Where** does the required data come from?
* **Who** is responsible for ensuring the availability and quality of the data?
* **When** do we receive data?
* **Why** do we need this specific set of data?

As with PARCS, the Five W's also serve as a guide, and in some instances only some of the W's might apply.

## Example

### Input

#### Story of the data

In a clean water network, the decision hypothesis of which supply lines need to be throttled, diverted or increased requires the input of data from various sources.
The main source of input data would be the volume measurements of service reservoirs, together with the pressure and flow measurements from well dispersed sensors throughout the network.
This measurement data needs to be of a time series nature, and for flow and pressure, directionality is also of importance.
Directionality indicates in which direction along the supply line the water is flowing, or in which direction the pressure differential exists.
Each measurement therefore needs to consist of a timestamp, a unique name/label/tag for identification and a measurement value.
For each measurement tag, record needs to be kept of the engineering unit of the unit of measure the tag's values represent.
In addition, the network itself needs to be described geographically such that  the concept of containment is captured. 
For example, a flow metered zone (FMZ) resides in a hydraulic system, which resides in a geographic area, which in turn resides in a geographic region.
For each measurement tag, record need to be kept of where in the network it resides.
All of this record keeping needs to account for changes over time such that it will always be possible to establish the entire state of the network at any given previous point in time.
For example, in the event that the network hierarchy changes (either by the growth or reduction of the size of a hydraulic system), it should always be possible to reconstruct the original topology.
Timely supply of measurement values are required, to a granularity of one measurement for each tag for every 15 minutes.
Precipitation levels for various geographic areas and even down to  hydraulic system level greatly influences supply and demand. 
This precipitation data takes the form  of historic, current and 7-day forecasts, with a granularity of 5 minutes.

> We start out by writing down the story of the data as we currently have it.
> Using the Five W's of Data, we iterate over our initial formulation to make sure we answer as many of the W's as possible.

##### Actors

* **Customers** consuming clean water and expecting uninterupted supply of clean water
* **Operations Engineer** responsible for monitoring and managing supply and demand in the network
* **Clean water** distributed by the network and consumed by customers
* **Water treatment works** (WTW) producing clean water for distirbution and eventual consumption by the network
* **Service reservoirs** (SR) providing temporary storage capacity for clean water
* **Flow measuring sensors** recording the rate of clean water flow at specific points
* **Pressure measuring sensors** recording the pressure of the clean water at specific points
* **Volume measuring sensors** recording the volume of clean water available in service reservoirs
* **Precipitation levels** per hydraulic system, every 5 minutes.

> Here we make use of the **Who**, **What** and **Where** of the Five W's to assist our formulation.

##### Setting

* **Geographic region** the clean water network is situated in
* **Geographic areas** the region is divided  into
* **Hydraulic systems** representing a further subdivision of areas
* **Flow metered zones** (FMZ), representing a subdividsion of hydraulic systems
* **Network map** of where the various sensors and service reservoirs are located, and how everything is connected 
* **Precipitation levels**: historic, current and future per day per hydraulic system.

> Here we make use of the **Where** of the Five W's to assist our formulation.

##### Plot

1. On a continuous basis, operational engineers monitor and manage the clean water supply such that demand, caused by customer consumption, is met at all times.
1. Managing the supply and demand involves, among other things, attending to abnormalities in the network such as blockages, leakages, pump or valve failures.
1. Managing supply and demand also involve throttling and redirecting flow, and switching on and off of pumps transferring water between service reservoirs.
1. Because water takes time to flow, operational engineers need to know in advance the predicted supply and demand throughout the network so that they can respond before demand exceeds supply.
1. As an added input, precipitation levels greatly affects supply and demand in the entire network, so any prediction needs to take precipitation levels into account.

> Here we ask all of the W's: **Who**, **What**, **Where**, **When** and **Why** of the Five W's to assist our formulation.

##### Conflict

* WTW supply of clean water  and customer consumption are both dynamic.
* Faults in the network, which may include blockages, pump failures or leakages in pipes or reservoirs happen at random and can severely impact the network's ability to satisfy demand.
* Precipitation levels greatly affects supply and demand in the entire network.
* Operational engineers need to know well in advance if a potential supply shortage might occur, and exactly where so that mitigating actions can be taken.

> Again, here we ask all of the W's: **Who**, **What**, **Where**, **When** and **Why** of the Five W's to assist our formulation.

##### Resolution

* Even though there is a high degree of variability and dynamicity inherent in the system, there seems to be higher-order patterns that emerge over time and through the seasons of the year.
* These paterns, along with analysis of rates of change can be exploited to predict the expected future supply and demand.

> Again, here we ask all of the W's: **Who**, **What**, **Where**, **When** and **Why** of the Five W's to assist our formulation.

### Output

#### Story of the data

Operational engineers require a global overview of the entire state of the network in the form of maps and diagrams representing the network topology.
This global overview needs to contain analytics in the form of aggregations  representing the current level of detail.
The current level of detail is the hierarchy level at which the global overview is being viewed at: region, area, system or FMZ. 
Overlayed on top of the global overview, the operational engineers require colour-coded and symbology to communicate health levels of the supply and demand situation.
Based on historic data, a set of data science predictive models generate a 24-hour forecast of the demand of the network, which also gets overlayed on maps and diagrams.
Additionally, alerts need to be raised if the current situation is likely to lead to demand that cannot be met by the supply.

##### Actors

No new actors enter the story, and all the actors from the input data requirements apply.

##### Plot

* Based on historic data, a set of data science predictive models generate a 24-hour forecast of the demand of the network.
* This forecast gets presented as a forward-looking simulation of the network demand.
* The operational engineers can use the forecast to get a highly probable perspective on the demand situation as it will be 24 hours in the future.
* Based on this probable future, proactive action can be taken now.

##### Setting

No new setting elements enter the story, and all the setting elements from the input data requirements apply.

##### Conflict

* The demand forecast is only a prediction 24 hours into the future, with a level of uncertainty.

##### Resolution

* The forecast gets persisted, and when the real-world data arrives, the delta between the predicted values and actual values serve to improve the predictive model.


