# URI strategy

## Why



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


#### stop_points/{id}


#### connections




