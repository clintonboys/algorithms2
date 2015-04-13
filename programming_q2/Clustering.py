import pandas as pd

frame = pd.read_csv('clustering1.txt',skiprows=1,delim_whitespace=True,header=0,names=['edge_1','edge_2','cost'])

## start off with each point in a separate cluster

## repeat until only k clusters:
	## let p,q be closest pair of separated points
	## merge the clusters containing p, q into a single cluster



def FindClosestPair(graph):

	return None

def Merge(cluster1,cluster2):

	return None