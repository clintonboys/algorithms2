class UnionFind:

    def __init__(self, n):

        self._id = range(0,n)
        self._count = n
        self._rank = [1]*n

    def find(self,p):

        id = self._id
        while p != id[p]:
            id[p] = id[id[p]]   # Path compression using halving.
            p = id[p]
        return p

    def count(self):
    	return self._count

    def check_connected(self,p,q):
    	return self.find(p) == self.find(q)

    def union(self,p,q):

    	id = self._id
    	rank = self._rank

    	i = self.find(p)
    	j = self.find(q)

    	if i == j:
    		return

    	if rank[i] < rank[j]:
    		id[i] = j
    	elif rank[j] > rank[i]:
    		id[j] = i
    	else:
    		id[j] = i
    		rank[i] = rank[i] + 1

    def num_clusters(self):

    	return len(set(self._id))