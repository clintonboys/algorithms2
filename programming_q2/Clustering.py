import pandas as pd
from pandas import DataFrame
from UnionFind import UnionFind

frame = pd.read_csv('clustering1.txt',skiprows=1,delim_whitespace=True,header=0,names=['edge_1','edge_2','cost'])

## start off with each point in a separate cluster

## repeat until only k clusters:
	## let p,q be closest pair of separated points
	## merge the clusters containing p, q into a single cluster

graph = UnionFind(500)

frame = frame.sort(['cost'],ascending = True)
frame.index = range(0,len(frame))

for i in range(0,len(frame)):
	if graph.num_clusters() > 4:
		if not graph.check_connected(frame['edge_1'][i]-1, frame['edge_2'][i]-1):
			graph.union(frame['edge_1'][i]-1, frame['edge_2'][i]-1)
	else:
		pass
 

def GetMinSpacing(graph, frame):

	lengths = []

	for i in range(0,len(frame)):
		if graph._id[frame['edge_1'][i]-1] != graph._id[frame['edge_2'][i]-1]:
			lengths.append(frame['cost'][i])

	return min(lengths)

print GetMinSpacing(graph, frame)