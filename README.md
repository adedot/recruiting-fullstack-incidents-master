# Recruiting Take Home Assignment


## Generate geojson
1. `python3 -m venv env`
2. `source env/bin/activate`
3. `python -m pip install --upgrade pip`
4. `pip install -r requirements.txt`
5. `python etl-geojson.py`

    data.geojson will be appear in the home directory

The data in the directory should look something like

```
{
	"type": "FeatureCollection",
	"features": [{
		"type": "Feature",
		"properties": {
			"name": "MEDIA GENERAL - TIMES DISPATCH 333 E FRANKLIN ST Richmond"
		},
		"geometry": {
			"type": "Point",
			"coordinates": [-77.440624, 37.541885]
		}
	}, {
		"type": "Feature",
		"properties": {
			"name": "CANDLEWOOD SUITES 4301 COMMERCE RD Richmond"
		},
		"geometry": {
			"type": "Point",
			"coordinates": [-77.428683, 37.466513]
		}
	}]
}

```

sample.geojson has sample geojson data based on the json files in /data folder

## Install needed packages
npm install .

## Start map application
node server.js

## Go to link

http://127.0.0.1:3000/


Incident Map
![Incident Map](leaflet-map-example.png)


# Improvements/TODO items if given more time

If I was given more time, I would do the following: 

* Refactor repeating code
* Add car incident as a polygon possibly
* Create Rest Api using fast api
* Put data in Postgres database using postgis and gdal
* Data analysis of incidents using python

 I spent an estimated 4  - 6 hours on this project