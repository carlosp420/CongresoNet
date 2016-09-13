import json
import requests
import yaml


with open("person_names.yml", "r") as handle:
    data = yaml.load(handle.read())


matrix = dict()

API_URL = "http://www.proyectosdeley.pe/api/congresista.json/"
for person_name in data:
    url = "{}{}".format(API_URL, person_name)
    res = requests.get(url)
    result = res.json()
    if "error" not in result:
        for person in result['resultado']:
            name = person['nombre']
            projects = person['proyectos']
            if projects:
                matrix[name] = projects


with open("person_projects.json", "w") as handle:
    handle.write(json.dumps(matrix, indent=4, sort_keys=True))
