from VendingMachine.service.beverage_service_interface import BeverageInterface
from VendingMachine.models.beverage import Beverage

class BeverageService(BeverageInterface):
	beverageDetails = {}

	def addBeverage(self,id,name,ingredients):
		"""
		Add beverage
		"""
		beverage = Beverage()
		beverage.setId(id)
		beverage.setName(name)
		beverage.setIngredient(ingredients)
		self.__class__.beverageDetails[id] = beverage

		return beverage