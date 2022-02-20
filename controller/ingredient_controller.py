class IngredientController(object):
	def __init__(self, IngredientService):
		self.IngredientService = IngredientService

	def addIngredient(self,id,name,quantity):
		return self.IngredientService.addIngredient(id,name,quantity)