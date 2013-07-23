# URI strategy

## Why

We need to agree on a URI strategy before giving ids to everything in the world. Each new version of this URI strategy has to be backwards compatible.

## Strategy

The root: http://stations.io/

Further paths' semantics follow the opentransport vocabulary:

### /{object}/

Object can be:

#### stop_areas/{id}

Gives a list of all stop_areas if no id is given. If an id is given, it will return the information about stop_area, with this included:
 * links to the stop_points the area contains
 * administrative region (contains links to geonames)
 * links to connections
 * ...

#### stop_points/{id}

Gives a list of all stop_points if no id is given. If an id is given, it will return the information we have about this stop_point and the relation to the other things in our system.

#### connections/{id}

Gives a list of all connections if no id is given. If an id is given, it will return the information about connection and the relation to the other things in our system.


