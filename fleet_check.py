import requests

#postman mock server url and endpoint
base_url = "POSTMAN_MOCK_URL_HERE"
endpoint = "/fleet/vehicles" 

#postman API key
api_key = "POSTMAN_API_KEY_HERE"
credential = {"X-API-Key": api_key}

#make the API call
response = requests.get(base_url + endpoint, headers=credential)

#parse the JSON
data = response.json()
vehicles = data["data"]

alerts = []
active_count = 0

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

# Count Active Vehicles
    if engine == "On":
        active_count += 1

# Alert: idling (engine on, not moving)
    if engine == "On" and speed == 0:
        alerts.append("Warning - " + name + ": Idling")

#Alert: low fuel
    if fuel < 25:
        alerts.append("Warning - " + name + ": Low Fuel (" + str(fuel) + "%)")

# Alert: no driver assigned
    if driver == "unassigned":
        alerts.append("Warning - " + name + ": No Driver Assigned")

#Pring alerts section
print("\nALERTS")
print("------")
if len(alerts) == 0:
    print("No alerts - all vehicles nominal")
else: 
    for alert in alerts:
        print(alert)

# Print summary section
print("\nSUMMARY")
print("-------")
print("Total Vehicles: " + str(len(vehicles)))
print("Active:         " + str(active_count))
print("Alerts triggered: " + str(len(alerts)))
print("\n=================================================================")


print ("Done")