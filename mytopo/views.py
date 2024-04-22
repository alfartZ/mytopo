from django.shortcuts import render
import requests, json

# Create your views here.
def index(req):
    url = "http://10.34.1.204:8000/ajax/try/get_topo_raw"
    headers = {
        "Cookie" : "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImN5ZDlNbXJDc2xKcGFwSHVEMWlxSEE9PSIsInZhbHVlIjoiTUxPQzVOMzNmemZGSFR6RFozNTRHOStNR1FSYWhrVzZiMEl4NjVrUnJEeDFUNmJmckY2Rm8yLzI3ZzJnY2ZnMW1Ud1R6aDNHL05IYXhDcWNJQXNQWWxPaTh6c0QyeFJHN1I1YXRxN1lHRXJQYlB6b21WR0lJZXRvdmlacVV3Y2FKUFNESUEwU0Z6bVFLazN2UStjbkV3STJSd2RQMWVpc2VrUUZEMENxT1poTEpvWksrWTBuUXNyUEtlaHdIdWtFM2hHbWo0RjdCalZrYzVSU2ZBdGY5eWxmbjlRd0J2RWo3N0YwU1MxNVd4Zz0iLCJtYWMiOiJiYWE1OGUxYzIwYTgxYzkxOTIxOGY3NzI5NWE5OWQ0NDE5ZjYwMGJhMzkyZjJmODE0M2Y1NmRkOTY3YThiYjE2IiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6Ijh6OThmY1V6Y0dtUDdUampXU0ljVVE9PSIsInZhbHVlIjoiYlptTXZxdkUwTnZCWmEvSEM5MGhlMjRxOFNEWWY4OU95cUZVNElFRFdBUzJmcHlhOG9uTUd6bzhEeEVTVmlPcUtkZkJPNWJzRDh3Yis3eFNiV0J4SnpwRFJ4NUdvQlFqRUN3cWZETVdqNHFEVFo5U0hwVkt5c1EwR0kxL0E4WjUiLCJtYWMiOiJlNDNjNDMwMWY2ODhhZDUxYmNkNDg0NWM2NjliNTkzYzFkZmEzOTRjNjc5OGI3NWJkY2VhZWVjYzc0M2JkYjgxIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IjRlam5DaXpqNzBPcGZra0NIUHJlV0E9PSIsInZhbHVlIjoidi80TWs1WWNlTnNiN1l3OExhOS80VVNKSi9ablFaRVR4TEM0RnhOOHZHOENXNVEzY0FCS3g5NGdLb0NoR2xTM0h1T2dlaUhwbWJucmRxVVI2UzRScUQzeHcwR0lLVEljeTF5cEZZbVpKQ2o2ZzZyNzhvQ01TcFc2VStwUWMrdFAiLCJtYWMiOiIzZDJjYjBhY2Y1NmZlNmI2ODYwMzgzNWVkNzdiYWFmNWYyY2VmOTIwOWE3ZTFiMzhjZTllZDMwMzZmZjM5NWI0IiwidGFnIjoiIn0%3D"
    }
    getter = requests.get(url, headers=headers).json()
    data = ["data1", "data2", "data3"]
    return render(req, 'index.html', {'data':data, 'getter':getter, 'nodes':json.loads(getter['nodes']), 'edges':json.loads(getter['edges'])})

def spog(req):
    url = "http://10.34.1.204:8000/ajax/try/get_topo_raw"
    headers = {
        "Cookie" : "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImN5ZDlNbXJDc2xKcGFwSHVEMWlxSEE9PSIsInZhbHVlIjoiTUxPQzVOMzNmemZGSFR6RFozNTRHOStNR1FSYWhrVzZiMEl4NjVrUnJEeDFUNmJmckY2Rm8yLzI3ZzJnY2ZnMW1Ud1R6aDNHL05IYXhDcWNJQXNQWWxPaTh6c0QyeFJHN1I1YXRxN1lHRXJQYlB6b21WR0lJZXRvdmlacVV3Y2FKUFNESUEwU0Z6bVFLazN2UStjbkV3STJSd2RQMWVpc2VrUUZEMENxT1poTEpvWksrWTBuUXNyUEtlaHdIdWtFM2hHbWo0RjdCalZrYzVSU2ZBdGY5eWxmbjlRd0J2RWo3N0YwU1MxNVd4Zz0iLCJtYWMiOiJiYWE1OGUxYzIwYTgxYzkxOTIxOGY3NzI5NWE5OWQ0NDE5ZjYwMGJhMzkyZjJmODE0M2Y1NmRkOTY3YThiYjE2IiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6Ijh6OThmY1V6Y0dtUDdUampXU0ljVVE9PSIsInZhbHVlIjoiYlptTXZxdkUwTnZCWmEvSEM5MGhlMjRxOFNEWWY4OU95cUZVNElFRFdBUzJmcHlhOG9uTUd6bzhEeEVTVmlPcUtkZkJPNWJzRDh3Yis3eFNiV0J4SnpwRFJ4NUdvQlFqRUN3cWZETVdqNHFEVFo5U0hwVkt5c1EwR0kxL0E4WjUiLCJtYWMiOiJlNDNjNDMwMWY2ODhhZDUxYmNkNDg0NWM2NjliNTkzYzFkZmEzOTRjNjc5OGI3NWJkY2VhZWVjYzc0M2JkYjgxIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IjRlam5DaXpqNzBPcGZra0NIUHJlV0E9PSIsInZhbHVlIjoidi80TWs1WWNlTnNiN1l3OExhOS80VVNKSi9ablFaRVR4TEM0RnhOOHZHOENXNVEzY0FCS3g5NGdLb0NoR2xTM0h1T2dlaUhwbWJucmRxVVI2UzRScUQzeHcwR0lLVEljeTF5cEZZbVpKQ2o2ZzZyNzhvQ01TcFc2VStwUWMrdFAiLCJtYWMiOiIzZDJjYjBhY2Y1NmZlNmI2ODYwMzgzNWVkNzdiYWFmNWYyY2VmOTIwOWE3ZTFiMzhjZTllZDMwMzZmZjM5NWI0IiwidGFnIjoiIn0%3D"
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