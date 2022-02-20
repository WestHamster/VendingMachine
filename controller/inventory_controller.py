import json

class InventoryController(object):
	def __init__(self,InventoryService):
		self.InventoryService = InventoryService

	def addItems(self,id,beverageId,name, stock, itemRequest):
		return self.InventoryService.addItems(id,beverageId,name,stock,itemRequest)

	def getIngredientBalance(self,ingredientId):
		balance = 0
		order_status = True

		for ingredientId in self.InventoryService.inventoryDetails:
			items = self.InventoryService.inventoryDetails.get(ingredientId)
			print("\n\nRequested Ingredients:",items.getItem())
			
			for key in items.getItem():
				#print(type(items.getStock().get(key)))
				new_bal = items.getStock().get(key)
				if key in items.getStock():
					new_bal = new_bal - items.getItem().get(key)
					if new_bal<0:
						return False
					items.getStock().update({key:new_bal})
					order_status = True

				else:
					return order_status

		return order_status