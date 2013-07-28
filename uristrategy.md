# URI strategy

## Why

We need to agree on a URI strategy before giving ids to everything in the world. Each new version of this URI strategy has to be backwards compatible.

## Strategy

All URIs will return a HTTP 303 towards this URL: {URI}.about.
This .about will check what format the client wants using content negotiation (or can be overwritten with ?format=...)

Formats to be supported: CSV, XML, JSON, RDF, TTL, N3

### The root: http://stations.io/

On this site the 

Further paths' semantics follow the OpenTransport vocabulary:

### /{object}/

Object can be:

#### stop_areas/{id}

Gives a list of all stop_areas if no id is given. If an id is given, it will return the information about stop_area, with this included:
 * links to the stop_points the area contains
 * administrative region (contains links to geonames)
 * links to connections
 * ...

For each different id system, a new alias system will also be put in place which the URLs will redirect to the general URI of stations.io. Thus `stop_areas/{alternative_system_name}/{alternative_id}` will redirect to `stop_areas/{id}`

#### stop_points/{id}

Gives a list of all stop_points if no id is given. If an id is given, it will return the information we have about this stop_point and the relation to the other things in our system.

For each different id system, a new alias system will also be put in place which the URLs will redirect to the general URI of stations.io. Thus `stop_points/{alternative_system_name}/{alternative_id}` will redirect to `stop_points/{id}`.

#### connections/{id}

Gives a list of all connections if no id is given. If an id is given, it will return the information about connection and the relation to the other things in our system.

