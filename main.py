import requests
a=requests.get("http://ip-api.com/json")
if a.status_code == 200:
    # Parse the JSON a
    data = a.json()
    print(data)
    