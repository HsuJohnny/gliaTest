from collections import Counter
urls=[
	'https://www.google.com.tw/a.txt',
	'https://www.google.com.tw/b.txt',
	'https://www.google.com.tw/tt/asd/c.txt',
	'https://www.google.com.tw/c.txt',
	'https://www.google.com.tw/b.txt',
	'https://www.google.com.tw/b.txt',
	'https://www.google.com.tw/a.txt',
	'https://www.google.com.tw/a.txt'
	]
flag = 0
filenames = []
for item in urls:
	filename=''
	l = len(item)
	rev = item[::-1]
	while(True):
		if(rev[flag]!='/'):
			filename=filename+rev[flag]
			flag = flag + 1
		else:
			break
	flag = 0
	temp = filename
	filenames.append(temp)
names=[]
for item in filenames:
	new_item = item[::-1]
	names.append(new_item)
l = len(names)
count = 0
rank = {}
history = []
for i in range(l):
	if(names[i] not in history):
		history.append(names[i])
		for x in range(i,l):
			if(names[x] == names[i]):
				count = count + 1
		rank[names[i]] = count
		count = 0

d = Counter(rank)
for k,v in d.most_common(3):
	print ('%s: %i'%(k,v))
