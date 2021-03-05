print ('Hola cazando apis')

import requests
import json

response = requests.get("https://swapi.dev/api/people/2")

print (response.text)

json_data = json.loads(response.text)

print (json_data['name'])
