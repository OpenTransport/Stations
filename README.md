# Stations

## Why this project?

### Problem

Identifying stuff in the transport field is a mess. In every certain field there are different identification methods and they are difficult to interconnect.

For example, when one dataset from a bus company is opened, it takes a lot of fiddling to make the right connections with a train company's dataset. Similar problems exist when programming things cross border (in different countries, the same stops/stations/things have different identifications) or even in the same datasets, to tell which stop is connected to another stop (sometimes they have the same name, in other cases they are a bit different (e.g. an extra id concatenated to the name)). 

### Proposed solution

Using the vocabulary we have discussed at [opentransport/vocabulary](http://github.com/opentransport/vocabulary) we will set up a site which can reuse data from various sources and link them all together.

## What should it look like?

It should have functions for three different end-users:
* Data owners: add a link for datadump of stops which can be automatically fetched. Provide mappings to the stations.io scheme.
* Data consumers: get the right datadump for your application with the right IDs from different systems
* Data enrichers: add data for one specific stop

### Extra data owner use cases
(e.g. an open street map contributor or a transport agency employee)

* Clean datasets and do named entity recognition
* Link to global `stop_area` and `stop_point` IDs
* -add yours-

### Extra data consumer use cases
(e.g. an app creator, a map designer or an accessibility researcher)

* An autocomplete list generator
* Get the right `connection_link` times to create links between modes
* -add yours-

### Extra data enricher use cases
(e.g. an app creator who wants to provide a feedback button in his app, an integrator who finds mistakes in the dataset, a transport company that is moderating the data, and so on)

* Being able to do PUT and POST requests on a URI
* A simple interface to view, edit and add feedback to a representation
* -add yours-

## Directory structure

To structure the files in this repository, we use the following hierarchy:

```bash
# Location of a list of stop_areas*
/data/{country_code}/{datasource_name}_areas.csv
# Location of a list of stop_points*
/data/{country_code}/{datasource_name}_points.csv
# Location of a list which links different points and areas together and describes potential connections between points or between different areas.
/data/{country_code}/{datasource_name}_relations.csv
# Extra file to describe relations between different datasources
/data/{country_code}/relations.csv
# An international list of stop areas
/data/international/{datasource_name}_points.csv
/data/international/{datasource_name}_areas.csv
/data/international/{datasource_name}_relations.csv
/data/international/relations.csv
# Describing similar identities between datasets of countries
/data/extra_relations.csv
```

* For the difference between a `stop_area` and a `stop_point`, check the (vocabulary)[https://github.com/opentransport/vocabulary]


### Headings

We use comma separated values. You can find the description using the [simple data format](http://dataprotocols.org/data-packages/)

#### {datasource_name}_areas.csv

```csv
//TODO
```


#### {datasource_name}_points.csv


```csv
//TODO
```

#### ({datasource_name}_)relations

```csv
stop uri 1 , stop uri 2 , relation type , value
```
