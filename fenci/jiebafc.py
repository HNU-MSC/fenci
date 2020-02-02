import jieba

f = open('assets/a.txt', 'r')
content = f.read()

print(content)

seg_list = jieba.cut(content)
fw = open('results/jiebaa.txt', 'w')

fw.write('\n'.join(seg_list))

f.close()
fw.close()
