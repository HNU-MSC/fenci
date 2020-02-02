import thulac
import json
from flask import Flask
from flask import render_template
from flask import request
from urllib.parse import unquote

thul = thulac.thulac()
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/cicloud')
def cicloud():
    return render_template('cipin.html')


@app.route('/fenci', methods=["POST"])
def fenci():
    text = request.form['text']
    seg_list = do_fenci(text)
    return json.dumps(seg_list, ensure_ascii=False)


def do_fenci(text):
    seg_list = thul.cut(text)
    return seg_list


@app.route('/cipin')
def cipin():
    f = open('../results/thulacming.txt', 'r')
    cipin_list = []
    for line in f:
        item = line.split(' ', 2)
        cipin_list.append([item[0], int(item[1])])
    return json.dumps(cipin_list, ensure_ascii=False)

@app.route('/ciming')
def ciming():
    f = open('force_directed.json', 'r', encoding='utf-8')
    res = json.loads(f.read())
    key = unquote(request.args.get('key', ''))
    data_json = {
        'nodes': [],
        'links': []
    }
    key_val = 0
    for item in res['links']:
        if item['source'] == key:
            data_json['links'].append(item)
            data_json['nodes'].append({
                'id': item['target'],
                'val': item['val']
            })
            key_val += item['val']
            
    data_json['nodes'].append({
        'id': key,
        'val': 10
    })
    return json.dumps(data_json)

def do_ciming():
    highP, lowP = read_noun()
    print("HighP noun num: ", len(highP))
    print("LowP noun num: ", len(lowP))
    f = open('res.txt', 'w')
    res = json.dumps(closest_highP(highP, lowP), ensure_ascii=False)
    f.write(res)
    f.close()
    return res

def read_noun():
    f = open('../results/thulacming.txt', 'r')
    thesold = 10
    highP = {}
    lowP = {}
    for line in f:
        item = line.split(' ', 2)
        if int(item[1]) >= thesold:
            highP[item[0]] = json.loads(item[2])
        else:
            lowP[item[0]] = json.loads(item[2])
    f.close()
    return highP, lowP

def computeDist(pos, arr):
    left = 0
    right = len(arr) - 1
    if pos < arr[0]:
        return arr[0] - pos
    if arr[len(arr)-1] < pos:
        return pos - arr[len(arr)-1]

    while left + 1 < right:
        mid = int((left + right) / 2)
        if arr[mid] < pos:
            if arr[mid+1] < pos:
                left = mid
            else:
                return min(abs(arr[mid+1]-pos), abs(pos - arr[mid]))
        elif arr[mid] > pos:
            if arr[mid-1] > pos:
                right = mid
            else:
                return min(abs(arr[mid]-pos), abs(pos-arr[mid-1]))
        else:
            return 0
    return min(abs(arr[left]-pos), abs(arr[right]-pos))
        
def closest_highP(highP, lowP):
    closest_highP_dict = {}
    counter = 0
    for lowP_c, arr in lowP.items():
        counter += 1
        if counter % 1000 == 0:
            print(counter, "/", len(lowP))
        min_dist = 9999999
        min_highP = ""
        for pos in arr:
            for highP_c, highP_arr in highP.items():
                tmp_dist = computeDist(pos, highP_arr)
                if tmp_dist < min_dist:
                    min_dist = tmp_dist
                    min_highP = highP_c
        closest_highP_dict[lowP_c] = [min_highP, min_dist]
    return closest_highP_dict
