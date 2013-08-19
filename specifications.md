# Stations database

## Database format

The database is stored as plain text format on https://github.com/OpenTransport/Stations.

This allows to:

* Have a history of a station and what changed
* Peer-review modifications to the database (like bulk import of a new network)
* Keep in synch a home-made variant of the database

New entries to the database are done by pull requests.

Tools must be developped to import the files to easy to use database.

## Identification

### Cannonical form

Every object is identified by an URI having the following structure:

    http://stations.io/{object_type}/{id}

This ID must be unique and stable over time.

The object type is defined in https://github.com/OpenTransport/vocabulary

The id, is randomly generated hex string. The motivations are the following:

* A station can be used by different operators with different IDs. We do not want to favor a single operator
* The ID of the operator is generally not reliable
* Geohash was suggested: however stations might be moved (usually bus stops, but sometimes even large railway stations)

### Aliases

Every object can be aliased in order to use the local ID in different systems (API id, OpenStreetMap id, Wikipedia page…).

Aliases have the following structure and are not considered stable.

    http://stations.io/{object_type}/{referential}/{id}


## Tables

The database consists of the following tables:

* stop points
* stop areas
* connection links

## Attributes

### Stop Areas and Stop Point

* Geometry (point, line or area)
* Names (translations, previous names…)
* Importance
* Modes


### Connection link

* lengths (in meters or seconds)
* accesibility (how many steps, elevators…)
* opening hours
