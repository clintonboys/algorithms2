import pandas as pd
from pandas import DataFrame
from UnionFind import UnionFind

frame = pd.read_csv('clustering1.txt',skiprows=1,delim_whitespace=True,header=0,names=['edge_1','edge_2','cost'])

graph = UnionFind(500)

frame = frame.sort(['cost'],ascending = True)
frame.index = range(0,len(frame))


def GetClosestSeparatedPoints(graph,frame):

	cost = frame['cost'][len(frame)-1]

	for i in range(0,len(frame)):
		if graph._id[frame['edge_1'][i]-1] != graph._id[frame['edge_2'][i]-1]:
			if frame['cost'][i] < cost:
				cost = frame['cost'][i]

	return cost

for i in range(0,len(frame)):
	if graph.components() > 4:
		graph.union(graph._id[frame['edge_1'][i]-1], graph._id[frame['edge_2'][i]-1])

print GetClosestSeparatedPoints(graph,frame)
