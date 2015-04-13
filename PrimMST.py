import pandas as pd
import numpy as np
from operator import attrgetter

class Vertex(object):

    def __init__(self, vertex_id):
        self._vertex_id = vertex_id
        self.inX = False

    @property
    def vertex_id(self):
        return self._vertex_id

    def __eq__(self, another_vertex):
        return self._vertex_id == another_vertex._vertex_id

    def __hash__(self):
        return hash(self._vertex_id)

class Edge(object):

    def __init__(self, start_vert, end_vert, weight):
        self._start_vert = start_vert
        self._end_vert = end_vert
        self._weight = weight

    def start_vert(self):
        return self._start_vert
    def end_vert(self):
        return self._end_vert
    def weight(self):
        return self._weight

    def __eq__(self, another_edge):
        return self._start_vert == another_edge._start_vert and self._end_vert == another_edge._end_vert and \
               another_edge._weight == self\
            ._weight

def Read(file):
	verts = []
	edges = []
	frame = pd.read_csv(file,skiprows=1,delim_whitespace=True,header=0,names=['vertex_1','vertex_2','cost'])
	for i in range(1,501):
		verts.append(Vertex(i))
	for i in range(0,len(frame)):
		sv = frame['vertex_1'][i]
		ev = frame['vertex_2'][i]
		wt = frame['cost'][i]
		edges.append(Edge(sv,ev,wt))

	return verts, edges

vertices, edges = Read('edges.txt')

X  = [Vertex(412)]
T = []
cost = 0
print X[0]._vertex_id

while len(X) < len(vertices):
	candidates_1 = filter(lambda edge: Vertex(edge._start_vert) in X and Vertex(edge._end_vert) not in X, edges)
	candidates_2 = filter(lambda edge: Vertex(edge._end_vert) in X and Vertex(edge._start_vert) not in X, edges)
	candidates = candidates_1 + candidates_2
	min_edge = min(candidates, key=attrgetter('_weight'))
	print min_edge._weight
	if min_edge in candidates_1:
		X.append(Vertex(min_edge._end_vert))
	else:
		X.append(Vertex(min_edge._start_vert))
	T.append(min_edge)
	cost = cost + min_edge._weight
	print len (X), cost



