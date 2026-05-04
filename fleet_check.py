import requests

#postman mock server url and endpoint
base_url = "POSTMAN_MOCK_URL_HERE"
endpoint = "/fleet/vehicles" 

#postman API key
api_key = "POSTMAN_API_KEY_PLACEHOLDER"
credential = {"X-API-Key": api_key}

#make the API call
response = requests.get(base_url + endpoint, headers=credential)

#parse the JSON
data = response.json()
vehicles = data["data"]

print("=================================================================")
print("                   FLEET ANALYSIS REPORT")
print("=================================================================")
print("VEHICLE STATUS")
print("--------------")




#loop through the vehicles and print their details
for vehicle in vehicles:
    name = vehicle["name"]
    engine = vehicle["engineState"]
    fuel = vehicle["fuelPercent"]
    speed = vehicle["location"]["speedMilesPerHour"]
    odometer = vehicle["odometerMeters"]
    lat = vehicle["location"]["lat"]
    lng = vehicle["location"]["lng"]
    if vehicle["currentDriver"] is None:
        driver = "unassigned"
    else:
        driver = vehicle["currentDriver"]["name"]

    print(name + " | Engine "+ engine + " | Fuel " + str(fuel) + "% | Speed " + str(speed) + " mph" + " | Odometer " + str(odometer) + " m" + " | Latitude " + str(lat) + " | Longitude " + str(lng) + " | Driver: " + driver )

print ("Done")