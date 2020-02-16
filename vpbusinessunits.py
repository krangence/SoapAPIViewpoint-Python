import viewpoint
import requests
import json

business_units = viewpoint.get_business_units()
projects = {}
for bu in business_units:
# Casts all projects for each business unit to dictionary 'projects'
   projects[str(bu['ID'])] = viewpoint.get_projects(str(bu['ID']))
url = 'webhook_url'
requests.post(url, data=projects)
print(json.dumps(projects))