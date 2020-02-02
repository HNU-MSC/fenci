import json

f = open('res.txt', 'r')
res = json.loads(f.read())
f.close()

nodes = []
links = []

for key, item in res.items():
    links.append({
        "source": item[0],
        "target": key,
        "val": item[1]
    })
    nodes.append({
        "id": key,
        "val": item[1]
    })

    exist = False
    for node in nodes:
        if node['id'] == item[0]:
            exist = True
            break
    if not exist:
        nodes.append({
            "id": item[0],
        })

data_json = {
    "nodes": nodes,
    "links": links
}

output = open('force_directed.json', 'w')
output.write(json.dumps(data_json, ensure_ascii=False))
output.close()