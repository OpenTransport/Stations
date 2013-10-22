# The Belgians directory

These are files containing names, IDs and location used by Belgian transport agencies.

## NMBS/SNCB

The file nmbssncb.csv contains a file with this header:

```csv
railtime_id,hafas_id,stop_area_names@nl,stop_area_names@fr,stop_area_names@en,dbpedia_uris,lon,lat
```

### Context

 * railtime is the website by Infrabel (the railway maintainer). The URIs used by this website contain URIs from this file.
 * Hafas is a route planner which uses their own IDs. These IDs are used by the BENE Hafas route planner.
 * DBPedia is the semantic (RDF) version of wikipedia. Using these URIs you can do SPARQL queries on http://dbpedia.org/sparql

### Caveat emptor!!

 * at this moment only the "nl" names are correct. The French and English names are copies.
 * The DBPedia uri's are a mere guess and many of them won't resolve. We need better NER over there

(Thanks to Hannes Van De Vreken for this lovely list)