class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

def hash_function(self,key,size):
	return key%size

def rehash(self,old_hash,size):
	return (old_hash+1)%size

#placing items in hash table
def put(self , key , data):
	hash_value = self.hash_function(key , len(self.slots))

	if (self.slots[hash_value] == None):
		self.slots[hash_value] = key
		self.data[hash_value] = data
	elif(self.slots[hash_value] == key):
		self.data[hash_value] = data
	else:
		next_slot = self.rehash(hash_value , len(self.slots))
		while (self.slots[next_slot]! = None and self.slots[next_slot]! = key):
			next_slot = self.rehash(next_slot , len(self.slots))

	if(self.slots[next_slot] == None):
		self.slots[next_slot] = key
		self.data[next_slot] = data
	else:
		self.data[next_slot] = data

def get(self,key):
	start_slot = self.hash_function(key , len(self.slots))

	data = None
	stop = False
	found = False
	pos = start_slot

	while(self.slots[pos]!=None and not found and not stop):
		if(self.slots[pos]==key):
			found = True
			data = self.data[pos]
		else:
			pos = self.rehash(pos , len(self.slots))
			if(pos == start_slot):
				stop = True
	return data

	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,data):
		self.put(key,data)