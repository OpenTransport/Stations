# NMBS/SNCB

SPARQL and DB-Pedia:

SELECT DISTINCT *
WHERE {
    ?station dbpedia-owl:agencyStationCode ?code ;
             dbpedia-owl:country dbpedia-nl:België ; geo:lat ?lat ; geo:long ?long .
 # OPTIONAL {    ?station  owl:sameAs ?otherlang . } .
}

And plotting these using Geojson.io: http://geojson.io/#gist:pietercolpaert/6372701

