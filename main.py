import requests
import json

response = requests.get("http://worldtimeapi.org/api/ip")

json_data = json.loads(response.text)

for value in json_data:
     printValue = str(value).title().replace('_', ' ')
     print(printValue+": "+str(json_data[value]))
