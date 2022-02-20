class BeverageController(object):
	def __init__(self,BeverageService):
		self.BeverageService = BeverageService

	def addBeverage(self,id,name,ingredients):
		return self.BeverageService.addBeverage(id,name,ingredients)