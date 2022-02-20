# initialise the models

class Beverage(object):
	def __init__(self):
		self.id = None
		self.name = None
		self.ingredients = None

	def setId(self,id):
		self.id = id

	def getId(self):
		return self.id

	def setName(self,name):
		self.name = name

	def getName(self):
		return self.name

	def setIngredient(self,ingredients):
		self.ingredients = ingredients

	def getIngredient(self):
		return self.ingredients
