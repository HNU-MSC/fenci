import json

with open('force_directed.json', 'r') as f:
    res = f.read()
    res = json.loads(res)
    print(res['nodes'])