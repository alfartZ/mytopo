from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bs4 import BeautifulSoup as Soup
import requests, json

api_token = "30e571936b3470184bccd5ee3db520eb"
base_api = "http://10.34.1.204:8000/api/v0"
headers = {"X-Auth-Token": api_token}

# Create your views here.
def index(req):
    url = "http://10.34.1.204:8000/ajax/try/get_topo_raw"
    headers['Cookie'] =  "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjFvejcrSWxKN25WeWdScFRIYWRaeWc9PSIsInZhbHVlIjoiUFpYb0E0Sm1sUmpkcEd0MTJrZHM5UWg5dzVjNVhVeFRBQXNlL1lPdWdIQ3VVY3puTlRiUTU5UEp1Q2loK2kzdkQzSXg2RW5oRFE0bnl2aDc0Qk1TUTE0aU9iY3czWFdmVVVIVGF6R3gxZFdnb0YxZVBna1RPazFUT21RdG9ZSHlHSktPMHIvSzkzUWZTYVlUS0k2SGxqVFdkNEdGelJPaDBvR1JQbkRLeDVOOUpIckRVV3dpN2VjRmVBNm9OUmFKYjZ4OEFxMXBFWGZ4TlNnZ1FaUzA4UG1odnNSZ0sxVjkvbkNvQVcwTVJsZz0iLCJtYWMiOiJhNmFlMjlhODhiMjJmMjg5NGZhZjU0M2ZjZWU5YTRkNTg5MGQxNGUzYzZiNDZmMzlhM2Q2MTFkMDYyM2FjZjFkIiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6IkJHWnlQelhGbld3UkRrNE5vaUNiT0E9PSIsInZhbHVlIjoiNWJaT1FyMzd2aG4vL3p1cW9NdlRDUG1OZzl2YlJTbHBZN0gwU2lCODB6bmY3MkJ5eHVURjlNa0IzdGhWZnd5N25VZjdsdEVnTTVaanBhdnlkd0w5bXlETHc5ZWJ6MzUzMWRoc2lVcDZYanl6VmlwWXA4Sm5KNERTZEFCZzJ0UW0iLCJtYWMiOiIxYzJkMjA5OGM2ZjYwNDA3ZjdmMzIyODMyZTU3Y2RiMjdlN2JiNjRjZjY3ZjE4ODYxYjE2NzRiZGJkODUxZDkzIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6InJqTnozcnUySUZka1FnNkN1VDRoRXc9PSIsInZhbHVlIjoibUtXMVFEZ3BqbC84eU5ROXhpWE1KcU5ISDB5SlEzSXdxZTZ0KzRmRkR3dEovU2IrODNrUVFkRzFUZDBlaGoyU2cwNUdOc1d2WW5HaCtXeU1GNGRmMVNaK2IvUnlPNnp0WU5OWjE0SndQcVpnZVdrYWFsL1NnNFVlelN1eC9PMlkiLCJtYWMiOiI5YmQyMmViZmQ3YjYxODU3Mjc4MjYyY2E3MzFmNzJhODkzOWRlNjljN2VkYzM5MTlhNTA5NGM3MjI4ZDY4MDlkIiwidGFnIjoiIn0%3D"
    getter = requests.get(url, headers=headers).json()
    data = ["data1", "data2", "data3"]
    return render(req, 'index.html', {'data':data, 'getter':getter, 'nodes':json.loads(getter['nodes']), 'edges':json.loads(getter['edges'])})

# get topology raw data
def spog(req):
    url = f"{base_api}/custom-api/get_raw_topology"
    getters = requests.get(url, headers=headers)
    getter = getters.json()

    retn = {
        'nodes' : getter['nodes'],
        'edges' : getter['edges'],
        'options' : getter['options'],
        'page' : 'dashboard'
    }

    return render(req, 'spog3/index.html', retn)

# get device health
def device_health(req, device_id):
    url = f"{base_api}/custom-api/health/processor/device/{device_id}"
    getters = requests.get(url, headers=headers).text
    return render(req, 'proccessor.html', {'response':getters})

def get_list_health(device_id, type):
    url = f"{base_api}/devices/{device_id}/graphs/health/{type}"
    getters = requests.get(url, headers=headers)
    return getters.text

def overview_health(req, device_id):
    url = f"{base_api}/devices/{device_id}/health"
    getters = requests.get(url, headers=headers).json()
    graph_list = []
    for graph in getters['graphs']:
        graph_list.append({'desc':graph['desc'], 'graph':get_list_health(device_id, graph['name'])})

    # print(json.dumps(graph_list, indent=2))
    return render(req, 'librenms/health/health_overview.html', {"graph_list":graph_list})

def view_processors(req, device_id):
    url = f"{base_api}/custom-api/health/processor/device/{device_id}"
    getters = requests.get(url, headers=headers).text
    parser = Soup(getters, 'html.parser')
    img_urls = [img['src'] for img in parser.find_all('img')]

    svgs = []
    for imgs in img_urls:
        svgs.append(get_svg(imgs.replace("&height=100&width=215", "&height=200&width=315")))

    panel_body = parser.find_all(class_='panel-body')

    i = 0
    for bodys in panel_body:
        bodys['style'] = 'display: flex; flex-wrap: nowrap;'
        for col in bodys.find_all(class_='col-md-3'):
            col.a.replace_with(Soup(svgs[i], 'html.parser'))
            i+=1

    return render(req, 'librenms/health/health.html', {'response':parser.prettify()})

def get_svg(url):
    headers['Cookie'] = "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjFvejcrSWxKN25WeWdScFRIYWRaeWc9PSIsInZhbHVlIjoiUFpYb0E0Sm1sUmpkcEd0MTJrZHM5UWg5dzVjNVhVeFRBQXNlL1lPdWdIQ3VVY3puTlRiUTU5UEp1Q2loK2kzdkQzSXg2RW5oRFE0bnl2aDc0Qk1TUTE0aU9iY3czWFdmVVVIVGF6R3gxZFdnb0YxZVBna1RPazFUT21RdG9ZSHlHSktPMHIvSzkzUWZTYVlUS0k2SGxqVFdkNEdGelJPaDBvR1JQbkRLeDVOOUpIckRVV3dpN2VjRmVBNm9OUmFKYjZ4OEFxMXBFWGZ4TlNnZ1FaUzA4UG1odnNSZ0sxVjkvbkNvQVcwTVJsZz0iLCJtYWMiOiJhNmFlMjlhODhiMjJmMjg5NGZhZjU0M2ZjZWU5YTRkNTg5MGQxNGUzYzZiNDZmMzlhM2Q2MTFkMDYyM2FjZjFkIiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6IkJHWnlQelhGbld3UkRrNE5vaUNiT0E9PSIsInZhbHVlIjoiNWJaT1FyMzd2aG4vL3p1cW9NdlRDUG1OZzl2YlJTbHBZN0gwU2lCODB6bmY3MkJ5eHVURjlNa0IzdGhWZnd5N25VZjdsdEVnTTVaanBhdnlkd0w5bXlETHc5ZWJ6MzUzMWRoc2lVcDZYanl6VmlwWXA4Sm5KNERTZEFCZzJ0UW0iLCJtYWMiOiIxYzJkMjA5OGM2ZjYwNDA3ZjdmMzIyODMyZTU3Y2RiMjdlN2JiNjRjZjY3ZjE4ODYxYjE2NzRiZGJkODUxZDkzIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6InJqTnozcnUySUZka1FnNkN1VDRoRXc9PSIsInZhbHVlIjoibUtXMVFEZ3BqbC84eU5ROXhpWE1KcU5ISDB5SlEzSXdxZTZ0KzRmRkR3dEovU2IrODNrUVFkRzFUZDBlaGoyU2cwNUdOc1d2WW5HaCtXeU1GNGRmMVNaK2IvUnlPNnp0WU5OWjE0SndQcVpnZVdrYWFsL1NnNFVlelN1eC9PMlkiLCJtYWMiOiI5YmQyMmViZmQ3YjYxODU3Mjc4MjYyY2E3MzFmNzJhODkzOWRlNjljN2VkYzM5MTlhNTA5NGM3MjI4ZDY4MDlkIiwidGFnIjoiIn0%3D"
    getsvg = requests.get(url, headers=headers)
    return getsvg.text