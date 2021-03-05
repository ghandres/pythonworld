import requests
import json

response = requests.get("https://swapi.dev/api/people")

json_data = json.loads(response.text)

print (json.dumps(json_data,indent=4))
