#!/usr/bin/python3
"""Alta3 Research | <your name here>
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests
import datetime
import reverse_geocoder as rg

URL = "http://api.open-notify.org/iss-now.json"

def main():
    """code goes below here"""
    response = requests.get(URL)
    print (response,"\n")
    resp = response.json()

    print (resp,"\n")
    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]
    epoch= resp["timestamp"]
    time = datetime.datetime.fromtimestamp(epoch)
    locator_resp= rg.search((lat, lon))
    city= locator_resp[0]["name"]
    country= locator_resp[0]["admin1"]

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timestamp: {time}
    Lon: {lon}
    Lat: {lat}
    City: {city}
    Country: {country}
    """)

if __name__ == "__main__":
    main()

