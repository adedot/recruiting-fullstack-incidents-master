import os
import json


def create_feature_json(full_address, longitude, latitude):

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
            features.append(create_feature_json(full_address, longitude, latitude ))
        
        if i == 'apparatus':

            
            status = data[i][0]['unit_status']
            if status.get('acknowledged'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " acknowledged"
                longitude = data[i][0]['unit_status']['acknowledged'].get('longitude')
                latitude = data[i][0]['unit_status']['acknowledged'].get('latitude')
                features.append(create_feature_json(full_address, longitude, latitude ))

            if status.get('arrived'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " arrived"
                longitude = data[i][0]['unit_status']['arrived'].get('longitude')
                latitude = data[i][0]['unit_status']['arrived'].get('latitude')
                features.append(create_feature_json(full_address, longitude, latitude ))
            
            if status.get('available'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " available"
                longitude = data[i][0]['unit_status']['arrived'].get('longitude')
                latitude = data[i][0]['unit_status']['arrived'].get('latitude')
                features.append(create_feature_json(full_address, longitude, latitude ))

            if status.get('cleared'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " cleared"
                longitude = data[i][0]['unit_status']['cleared'].get('longitude')
                latitude = data[i][0]['unit_status']['cleared'].get('latitude')
                features.append(create_feature_json(full_address, longitude, latitude ))
            
            if status.get('dispatched'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " dispatched"
                longitude = data[i][0]['unit_status']['dispatched'].get('longitude')
                latitude = data[i][0]['unit_status']['dispatched'].get('latitude')
                features.append(create_feature_json(full_address, longitude, latitude ))

            if status.get('enroute'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " enroute"
                longitude = data[i][0]['unit_status']['enroute'].get('longitude')
                latitude = data[i][0]['unit_status']['enroute'].get('latitude')
                features.append(create_feature_json(full_address, longitude, latitude ))
            
            if status.get('~'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " ~"
                longitude = data[i][0]['unit_status']['~'].get('longitude')
                latitude = data[i][0]['unit_status']['~'].get('latitude')
                features.append(create_feature_json(full_address, longitude, latitude ))

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