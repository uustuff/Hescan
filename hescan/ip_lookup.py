import requests

def lookup_ip(ip):
    print(f"[+] Looking up IP: {ip}")
    try:
        resp = requests.get(f"https://ipapi.co/{ip}/json/")
        data = resp.json()
        if 'error' not in data:
            print(f"IP: {data.get('ip')}")
            print(f"City: {data.get('city')}")
            print(f"Region: {data.get('region')}")
            print(f"Country: {data.get('country_name')}")
            print(f"Org: {data.get('org')}")
            print(f"Latitude: {data.get('latitude')}")
            print(f"Longitude: {data.get('longitude')}")
        else:
            print("IP lookup failed.")
    except Exception as e:
        print("Error in IP lookup:", e)
