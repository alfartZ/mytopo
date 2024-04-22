from django.shortcuts import render
import requests, json

# Create your views here.
def index(req):
    url = "http://10.34.1.204:8000/ajax/try/get_topo_raw"
    headers = {
        
    }
    getter = requests.get(url, headers=headers).json()
    data = ["data1", "data2", "data3"]
    return render(req, 'index.html', {'data':data, 'getter':getter, 'nodes':json.loads(getter['nodes']), 'edges':json.loads(getter['edges'])})

def spog(req):
    url = "http://10.34.1.204:8000/ajax/try/get_topo_raw"
    headers = {
        
    }
    getters = requests.get(url, headers=headers)
    getter = getters.json()

    retn = {
        'nodes' : getter['nodes'],
        'edges' : getter['edges'],
        'options' : getter['options']
    }

    print(json.dumps(retn, indent=2))
    return render(req, 'spog3/SPOG.html', retn)