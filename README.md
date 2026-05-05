# Samsara Mock Fleet Analysis Tool

A Python script that connects to a mock Samsara fleet API, pulls live vehicle data, and automatically generates a fleet status report with alerts and summary statistics.

---

## What It Does

- Authenticates with the Samsara API using a POSTMAN API token
-Retrieves all vehicles from the '\flee\vehicles' endpoint
- Analyzes each vehicle for operational issues
- Flags three alert conditions:
    - **Idling** - engine on with speed at 0 mph (fuel waste)
    - **Low fuel** - fuel level below 25%
    - **Unassigned driver** - no driver linked to the vehicle
- Saves a formatted fleet report to 'fleet_report.txt'

---

## Why It Matters

Idling and low fuel are two of the highest operational costs in fleet management. This tool surfaces those issues automatically so fleet managers can act immediately rather than manually reviewing vehicle data.

## How to Run It

### Prerequisites
- Python 3.x installed
- 'requests' library installed

'''bash
pip install requests
'''

### Setup
1. Clone this repository
2. Open 'fleet_check.py'
3. Replace the placeholder credentials with your own:

'''python
base_url = "YOUR_POSTMAN_MOCK_URL_HERE"   # or https://api.samsara.com
api_key  = "YOUR_POSTMAN_API_KEY_HERE"    # or your Samsara API token
'''
4. Run the script:

'''bash
python fleet_check.py
'''

5. Open 'fleet_report.txt' to view the generated report

---

## Sample Output

=================================================================
'''FLEET ANALYSIS REPORT
'''VEHICLE STATUS
'''Truck 14 | Engine: On | Fuel: 62% | Speed: 0 mph | Driver: Maria Santos
'''Truck 15 | Engine: On | Fuel: 18% | Speed: 47 mph | Driver: James Okafor
'''Truck 16 | Engine: Off | Fuel: 91% | Speed: 0 mph | Driver: Unassigned
'''ALERTS
'''WARNING - Truck 14: IDLING (engine on, speed 0)
'''WARNING - Truck 15: LOW FUEL (18%)
'''WARNING - Truck 16: NO DRIVER ASSIGNED
'''SUMMARY
'''Total vehicles:   3
'''Active:           2
'''Alerts triggered: 3

---

## How This Maps to Samsara's Real API

This script was built against a Postman mock server that mirrors Samsara's actual '\fleet\vehicles\ response structure. To run against a live Samsara account replace the two placeholder values with:

- `base_url` → `https://api.samsara.com`
- `api_key` → your Samsara API token from cloud.samsara.com

The script requires no other changes.

## Built With

- Python 3 (in Visual Code Studio)
- Postman Mock Server
- Samsara Fleet API structure

## Author

Gage Matzen
Built as a portfolio project for a Sales Engineer role at Samsara

