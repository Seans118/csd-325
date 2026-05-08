import json
import urllib.request

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

file = open("iss.txt", "w")
file.write("There are currently {result['number']} astronauts on the ISS:\n\n")

for person in result["people"]:
    file.write(person['name'] + " - onboard\n")

file.close()