class UnionFind(object):

	def __init__(self, N):

		self._size = self.N = N
		self._id = range(0,N)
		self._components = N

	def find(self,p):

		return self._id[self._id[p]]

	def union(self,p,q):

		if self._id[self._id[p]] == self._id[self._id[q]]:
			return
		else:
			if self._id.count(self._id[p]) <= self._id.count(self._id[q]):
				for i in range(0,self._size):
					if self._id[i] == p:
						self._id[i] = self._id[self._id[q]]
			else:
				for i in range(0,self._size):
			 		if self._id[i] == q:
			 			self._id[i] = self._id[self._id[p]]
			self._components = self._components - 1
			return

	def components(self):

		return self._components