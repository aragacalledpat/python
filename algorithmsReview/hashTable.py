class HashTable:
	"""My implementation of a hash table"""
	def __init__(self):
		self.table = [[] for x in range(2)]
		self.itemCount = 0;  #used for dynamically resizing the table

	def insert(self, key, value):
		index = self.__getIndex(key,len(self.table))

		#if the key is already here, delete it before re-adding it
		for item in self.table[index]:
			if item[0] == key:
				self.table[index].remove(item)
				self.itemCount -= 1

		#insert and update count
		self.table[index].append((key, value))
		self.itemCount += 1

		self.__adjustTableSizeIfNecessary()

	def delete(self, key):
		index = self.__getIndex(key,len(self.table))

		#remove the item if we can find it, if not do nothing
		for item in self.table[index]:
			if item[0] == key:
				self.table[index].remove(item)
				self.itemCount -= 1

		self.__adjustTableSizeIfNecessary()

	def search(self, key):
		index = self.__getIndex(key,len(self.table))
		for item in self.table[index]:
			if item[0] == key:
				return item[1]

	def __getIndex(self,key, size):
		return hash(key) % size

	def __adjustTableSizeIfNecessary(self):
		#if there are as many items as there are 'buckets' then grow the table
		if(self.itemCount == len(self.table)):
			self.__growTable()
		elif (self.itemCount < len(self.table) / 2):
			self.__shrinkTable()

	def __growTable(self):
		#make a new table that's twice as big
		newTable = [[] for x in range(len(self.table) * 2)]

		#rehash items from the old table into the new table
		for bucket in self.table:
			for item in bucket:
				index = self.__getIndex(item[0],len(newTable))
				newTable[index].append(item)
		self.table = newTable

	def __shrinkTable(self):
		#make a new table that's half as big
		newTable = [[] for x in range(len(self.table) / 2)]

		#rehash items from the old table into the new table
		for bucket in self.table:
			for item in bucket:
				index = self.__getIndex(item[0],len(newTable))
				newTable[index].append(item)
		self.table = newTable
