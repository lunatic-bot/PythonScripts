import requests 
import json 

response = requests.get("http://api.open-notify.org/astros.json")
# http://api.open-notify.org/astros.json
print(response.status_code)
print(response.json())


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())




