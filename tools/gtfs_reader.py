#! /usr/bin/env python

import sys
import csv
import os.path
import urllib

if len(sys.argv) < 4:
    print "Usage: {0} gtfs_files_directory region datasource_name [output_directory]".format(sys.argv[0])
    sys.exit(-1)

gtfs_stops = os.path.join(sys.argv[1], "stops.txt")
if not os.path.isfile(gtfs_stops):
    print "Fatal: {0} is not a file".format(gtfs_stops)
    sys.exit(-1)

output_dir = sys.argv[4] if len(sys.argv) == 5 else ""

data_source_name = sys.argv[3]
uri = lambda id: "http://stations.io/{0}/{1}/{2}".format(urllib.quote(sys.argv[2]), urllib.quote(data_source_name), urllib.quote(id))

stop_areas_path = os.path.join(output_dir, "{0}_areas.csv".format(data_source_name))
stop_areas = csv.writer(open(stop_areas_path, 'wb'))
stop_areas.writerow(["uri", "name", "lon", "lat"])

stop_points_path = os.path.join(output_dir, "{0}_points.csv".format(data_source_name))
stop_points = csv.writer(open(stop_points_path, 'wb'))
stop_points.writerow(["uri", "name", "lon", "lat"])

relations_path = os.path.join(output_dir, "{0}_relations.csv".format(data_source_name))
relations = csv.writer(open(relations_path, 'wb'))
relations.writerow(["stop_uri_1", "stop_uri_2", "relation", "value"])

stops = open(gtfs_stops)
stop_areas_count = 0
stop_points_count = 0
relations_count = 0
for stop in csv.DictReader(open(gtfs_stops, 'rb')):
    stop_uri = uri(stop["stop_id"])
    if not stop.has_key("location_type") or stop["location_type"] in ["0", ""]:
        stop_points.writerow([stop_uri, stop["stop_name"], stop["stop_lon"], stop["stop_lat"]])
        stop_points_count += 1
        if stop.has_key("parent_station"):
            relations.writerow([stop_uri, uri(stop["parent_station"]), "transport:belongs_to", ""])
            relations_count += 1
    elif stop["location_type"] == "1":
        stop_areas.writerow([stop_uri, stop["stop_name"], stop["stop_lon"], stop["stop_lat"]])
        stop_areas_count += 1

print "Info: wrote {0} stop points, {1} stop_areas and {2} relations".format(stop_points_count, stop_areas_count, relations_count)
