from heapq import heappush, heappop

class Sort():
	def __init__(self,x):
		self.data = x;
	def Bubble(self):
		for x in xrange(len(self.data)):
			for x in xrange(len(self.data)-1):
				if(self.data[x]>self.data[x+1]):
						tmp = self.data[x]
						self.data[x] = self.data[x+1]
						self.data[x+1] = tmp
		return self.data
	
	def Insertion(self):
		for i in xrange(len(self.data)):
			j = i
			while(j>0 and self.data[i]<self.data[j-1]):
				j-=1
			tmp = self.data[i]
			k = i
			while(k>j):
				self.data[k] = self.data[k-1]
				k-=1
			self.data[j] = tmp
		return self.data
	
	def Merge(self):
		if(len(self.data)==1):
			return self.data
		middle = len(self.data)/2
		left = Merge(self.data[0:middle-1])
		right = Merge(self.data[middle-1:len(self.data)-1])
		result = []*len(self.data)
		dPtr = 0
		lPtr = 0
		rPtr = 0
		while(dPtr<len(self.data)):
			if(lPtr == len(left)):
				result[dPtr] = right[rPtr]
				rPtr+=1
			elif(rPtr == len(right)):
				result[dPtr] = right[lPtr]
				lPtr+=1
			elif(left[lPtr]<right[rPtr]):
				result[dPtr] = left[lPtr]
				lPtr+=1
			else:
				result[dPtr] = right[rPtr]
				rPtr+=1
		return result
	
	def Heap(self):
		h = []
		for i in self.data:
			heappush(h,i)
		return [heappop(h) for i in range(len(h))]
	
	def Quick(self):
		pass
		
	def Radix(self):
		pass