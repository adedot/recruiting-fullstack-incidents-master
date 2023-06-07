import os
import json


def create_feature(full_address, longitude, latitude):

    # return "{\"type\": \"FeatureCollection\"," + \
    # "\"features\": [
    return "{ \"type\": \"Feature\", \"properties\": { \"name\": \""+ full_address+"\"}," +\
    "\"geometry\": { \"type\" : \"Point\", \"coordinates\" : [" +str(longitude) + "," +str(latitude)+ "]}}"
  
path = "./data/"
dir_list = os.listdir(path)

features = []
for file in dir_list:
    file = path +file
    # Opening JSON file
    json_file = open(file)

    data = json.load(json_file)

    for i in data:
        if i == 'address':
            full_address = data[i].get("common_place_name") + " "
            full_address += data[i].get("address_line1") +" " +data[i].get("city")
            print(full_address)
            longitude = data[i].get('longitude')
            latitude = data[i].get('latitude')
            features.append(create_feature(full_address, longitude, latitude ))

geojson = "{\"type\": \"FeatureCollection\"," + "\"features\":["
number_of_features = len(features)
for index in range(number_of_features):
    geojson += features[index]
    if index < number_of_features - 1:
        geojson += ","
geojson += "]}"

output_file = open("data.geojson", "w")
output_file.write(geojson)
output_file.close()