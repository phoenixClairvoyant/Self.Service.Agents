# Relativistic model

* Since this model deals with temporal, spacial, historical, granularity and the *Five V's* of big data, we name this model the relativistic model. 
* We introduce the relativistic model to give ample thought space towards big data related concerns and requirements - something not traditionally dealt with in data modelling exercises.

## Five V's of Big Data
The "Five V's" is a helpful framework for ensuring that we think about all the relativistic aspects of the data we are modelling.
It is not essential that we say something about each of the Five V's, but it is crucial that we speak of temporal, spacial, historicity, granularity and positioning on the stream-batch continuum for as much of the data as possible.
**The "Five V's" are**:

* **Volume** referring to the amount or quantity of data for each entity and relationship, along with their attributes;
* **Velocity** referring to the speed at which data is generated, transmitted and received or delivered;
* **Variety** referring to the diversity among sources of data; 
* **Veracity** referring to the quality and accuracy, completeness and overall level of trust in the data, and
* **Value** referring to the degree of utility obtainable from the data, and in our context, to what degree the data enables decision making. 

## Stream-batch continuum 
Another useful backdrop for framing relativistic-related aspects of the data is the stream-batch continuum.

The stream-batch continuum can be described as a one dimensional line, with instantaneous real-time at the one extreme, and infinitely batched or delayed delivery at the other. 
It is hypothesised that all data resides somewhere along the stream-batch continuum.

## Historicity
How accurate and relevant is historical data, and how much historical data is required in order to drive the decision hypothesis.

## Granularity
What resolution is a particular data source available in, or how finely-grained do we require the data to be in order to satisfy the decision.

## Reasons if possible
In specifying the various relativistic aspects of the data required in order to enable the decision hypothesis, we try at all times to provide reasons for each.

## Requirement vs inherent attribute
The relativistic elements of the data model is a mix  between requirements and inherent attributes of the data.
Sometimes, a relativistic attribute of the data is not exactly a requirement, but simply an attribute of the data.
Other times, a hard requirement exists, and it is helpful to highlight these sooner rather than later.


## Persona audience

* Customer-capability
* Technical-capability

## Example

### Input

#### Five V's

* Because the data relating to the network hierarchy, the list of measurement tags, and the list of service reservoirs are all defined in a flat file, we will treat them together here. 
* We will term this data "configuration data".
* The time series measurement values of pressure, flow and reservoir volume we will term "telemetry data".
* The precipitation data, which have historic, current and forecast components per day per hydraulic system we will term "environmental measurements".

##### Configuration data

###### Volume
* Configuration data volume requirements are very low, being in the order of tens of megabytes or tens of thousands of individual entities.
* The volume requirements on configuration data is low because the physical network is bounded and grows very slowly over time.

###### Velocity
* Configuration data velocity requirements are very low, and this type of data is expected to change at most daily, more realistically no more than weekly or even monthly.
* Some aspects of configuration data might never change, or at most quarterly.
* The low velocity of configuration data is due to the slow growth and very conservative modification of the network.

###### Variety
* Even though configuration data is all flat file defined, the variety of ways in which the same data is represented takes on a diverse number of forms.
* This is especially true for relationships among the various entities.
* There are many variations of configuration data, which pose a challenge, and presents a risk.
* The variety requirement of the data is therefore relatively high for this system.

###### Veracity
* There is a low level of trust in the configuration data due to the poor quality, low accuracy and incompleteness of the data.
* This is primarily due to the flat file format (Excel) and the human-in-the-loop business process that produce the data.

###### Value
* The value that can be derived from the configuration data is significant such that it trumps the other negative V's.

##### Telemetry data

###### Volume
* The volume of the telemetry data is much higher than the configuration data.
* Telemetry data consists of tens of thousands of data points, delivered every 15 minutes.
* There also exists historical telemetry data for multiple years, which greatly increase the overall volume.
 
###### Velocity
* Telemetry data needs to be produced every 15 minutes for each measurement tag.
* The 15-minute granularity requirement exists due to the need of the system to surface state that is no more than 30 minutes delayed.

###### Variety
* Because there are only effectively three types of measurement tags: pressure, flow and reservoir volume, the variety is low.
* in addition, since these are engineering measurements, the possible range that values may assume are well-known in advance.

###### Veracity
* The telemetry data is highly trusted because it is entirely machine-generated.
* Because the data is machine-generated, it is highly predictable, and erroneous data is easily identified.
 
###### Value
* Telemetry data is highly valued since it enables machine learning and predictive modelling.

##### Environmental measurements

###### Volume
* Since precipitation measurements are historic, current and 7-days into the future, for all hydraulic systems, the overall volume of data can be relatively large.

###### Velocity
* Measurements are per 5 minutes, per hydraulic system.

###### Variety
* The precipitation measurements  value ranges are well-known in advance, so it is not varied.

###### Veracity
* The precipitation measurements are obtained from a third-party service and are highly tursted.

###### Value
* Because the precipitation measurements play a significant role in supply and demand, the value of this data is relatively high.

#### Stream-batch continuum

* Configuration data is highly batched, and changes are very rare.
* Telemetry data is highly stream-oriented and constantly change.
* Precipitation measurements are highly stream-oriented but do not change frequently in the course of a day.

#### Granularity
* Configuration data is granular enough to identify each entity uniquely.
* Telemetry data has a granularity of at most one value per measurement tag every 15 minutes, but it can be fewer for some tag types.
* Precipitation measurement have a granularity of one measurement per hydraulic system at most every 5 minutes.

#### Historicity
* Configuration data has a low historicity requirement because there does not exist historic records for past configurations.
* Telemetry data has a relatively high requirement in terms of historicity becausethe data is used for training a ML model.
* Precipitation measurements have very accurate historic data used in the ML model training, so the historicity requirement is high.


### Output


