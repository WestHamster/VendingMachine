from VendingMachine.service.ingredient_service_interface import IngredientInterface
from VendingMachine.models.ingredient import Ingredient


class IngredientService(IngredientInterface):
	ingredientDetails = {}

	def addIngredient(self,id,name,quantity):
		ingredient = Ingredient()
		ingredient.setId(id)
		ingredient.setName(name)
		ingredient.setQuantity(quantity)

		self.__class__.ingredientDetails[id]= ingredient

		return ingredient
