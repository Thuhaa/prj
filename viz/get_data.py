import requests
import json

# Declare the API Key
# Note that declaring an API KEY directly in the source code is unsafe
API_KEY = "002c85f0"

def retrieve_data():
	"""
	Retrieve the data from an API endpoint and create a list of features
	"""
	url = f"https://my.api.mockaroo.com/houses.json?key={API_KEY}"
	response = requests.get(f"https://my.api.mockaroo.com/houses.json?key={API_KEY}")
	data = json.loads(response.content)
	return data


def generate_geojson():
	"""
	Generate a GeoJSON file from the returned data above
	"""

	# Declare a geojson data template as shown
	geojson_template = {
	"type":"FeatureCollection",
	"features":[]
	}

	data = retrieve_data()

	# Iterate through the list of dicts from the retrieve_data function
	# and append the features accordingly
	for entry in data:
		geojson_template["features"].append(
			{
			"type":"Feature",
			"properties":{
				"image_thumbnail":entry["picture"], 
				"Type":entry["apartment_type"], 
				"Price":entry["price_per_unit"]},
			"geometry":{
				"type":"Point",
				"coordinates":[
					entry["longitude"],
					entry["latitude"]				]
			}
		}
	)
	geojson = geojson_template
	return geojson