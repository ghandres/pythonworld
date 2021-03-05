print ('Hola cazando apis')

import requests
import json

response = requests.get("https://swapi.dev/api/people/2")

json_data = json.loads(response.text)

print (json.dumps(json_data,indent=4))

print (json_data['name'])
