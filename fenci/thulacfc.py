import thulac

f = open('assets/db.txt', 'r')
content = f.read()

thul = thulac.thulac()

seg_list = thul.cut(content)

fw = open('results/thulacdb.txt', 'w')

name_dict = {}
for ci in seg_list:
    if ci[1].startswith('n'):
        if ci[0] in name_dict:
            name_dict[ci[0]] += 1
        else:
            name_dict[ci[0]] = 1
name_list = []
for k, v in name_dict.items():
    name_list.append([k, v])

name_list.sort(key=lambda item: item[1], reverse=True)

for item in name_list:
    fw.write(item[0] + ' ' + str(item[1]) + '\n')

f.close()
fw.close()
