import os
import json


def create_feature(full_address, longitude, latitude):

    feature =  "{ \"type\": \"Feature\", \"properties\": {"
    if full_address:
        feature += "\"name\": \""+ full_address+"\"}," 
    else: 
        feature += "\"}," 
    feature += "\"geometry\": { \"type\" : \"Point\", \"coordinates\" : [" +str(longitude) + "," +str(latitude)+ "]}}"
    
    return feature

path = "./data/"
dir_list = os.listdir(path)

features = []
for file in dir_list:
    file = path +file
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
        # if i == 'apparatus':

        #     full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
        #     status = data[i][0]['unit_status']
        #     if status.get('acknowledged'):
        #         full_address +=  " acknowledged"
        #         longitude = data[i][0]['unit_status']['acknowledged'].get('longitude')
        #         latitude = data[i][0]['unit_status']['acknowledged'].get('latitude')
        #     features.append(create_feature("", longitude, latitude ))


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