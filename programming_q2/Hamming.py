import pandas as pd
from pandas import DataFrame
from UnionFind import UnionFind

frame = pd.read_csv('clustering_big.txt',skiprows=1,delim_whitespace=False,header=0,names=['bit'])
frame = DataFrame.drop_duplicates(frame)
frame.index = range(0,len(frame))

def HammingDistance(list1,list2):
	dist = 0
	for i in range(0,len(list1),2):
		if list1[i] != list2[i]:
			dist = dist + 1
	return dist

def Count(list1,j):
	count = 0
	for i in range(0,len(list1),2):
		if list1[i] == str(j):
			count = count + 1
	return count

twobit = []

for i in range(0,24):
	for j in range(i,24):
		list2 = []
		for k in range(0,48):
			if k%2 == 0:
				if k == 2*i or k == 2*j:
					list2.append('1')
				else:
					list2.append('0')
			else:
				list2.append(' ')
		twobit.append(''.join(list2))

def Xor(list1,list2):
	result = []
	for i in range(0,len(list1)):
		if i%2 == 0:
			if list1[i] == '0' and list2[i] == '0':
				result.append('0')
			elif list1[i] == '0' and list2[i] == '1':
				result.append('1')
			elif list1[i] == '1' and list2[i] == '0':
				result.append('1')
			else:
				result.append('0')
		else:
			result.append(' ')
	return ''.join(result)

xorlist = []
for list1 in twobit:
	for list2 in twobit:
		xorlist.append(Xor(list1,list2))

xorlist = list(set(xorlist))

final_xorlist = []

print len(frame['bit'][0])
print len(xorlist[0])

for i in range(0,len(xorlist)):
	if xorlist[i] in frame['bit'].values:
		final_xorlist.append(xorlist[i])





