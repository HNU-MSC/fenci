import thulac

f = open('assets/ming.txt', 'r')
thul = thulac.thulac()

seg_list = []
i = 0
for line in f:
    seg_list.extend(thul.cut(line))
    if i % 1000 == 0:
        print(i)
    i += 1

print("finish fenci!")
fw = open('results/thulacming.txt', 'w')

name_dict = {}
name_index = {}
ii = 0
for ci in seg_list:
    if ci[1].startswith('n'):
        if ci[0] in name_dict:
            name_dict[ci[0]] += 1
            name_index[ci[0]].append(ii)
        else:
            name_dict[ci[0]] = 1
            name_index[ci[0]] = [ii]
    ii += 1

name_list = []
for k, v in name_dict.items():
    name_list.append([k, v, name_index[k]])

name_list.sort(key=lambda item: item[1], reverse=True)

for item in name_list:
    fw.write(item[0] + ' ' + str(item[1]) +
             ' ' + str(item[2]) + '\n')

f.close()
fw.close()
