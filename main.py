import requests
import json
import pprint

response = requests.get("http://worldtimeapi.org/api/ip")

json_data = json.loads(response.text)

# pprint.pprint(json_data)

for value in json_data:
     printValue = str(value).title().replace('_', ' ')
     print(printValue+": "+str(json_data[value]))
