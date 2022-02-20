
class Ingredient(object):
	def __init__(self):
		self.id = None
		self.name = None
		self.quantity = None

	def setId(self,id):
		self.id = id

	def getId(self):
		return self.id

	def setName(self,name):
		self.name = name

	def getName(self):
		return self.name

	def setQuantity(self,quantity):
		self.quantity = quantity

	def getQuantity(self):
		return self.quantity