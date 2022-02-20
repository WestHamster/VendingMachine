
class InventoryItem(object):
	def __init__(self):
		self.id = None
		self.beverageId = None
		self.name = None
		self.stock = {}
		self.itemRequest = {}

	def setId(self,id):
		self.id = id

	def getId(self):
		return self.id
	
	def setBeverageId(self,beverageId):
		self.beverageId = beverageId

	def getBeverageId(self):
		return self.beverageId

	def setName(self,name):
		self.name = name

	def getName(self):
		return self.name
	
	def setStock(self,stock):
		self.stock = stock

	def getStock(self):
		return self.stock

	def setItem(self,itemRequest):
		self.itemRequest = itemRequest

	def getItem(self):
		return self.itemRequest


"""
stock -> {"water":2, "coffee":3, "tea":2}
itemRequest -> {"water":1,}
"""