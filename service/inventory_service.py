from VendingMachine.service.inventory_service_interface import InventoryInterface
from VendingMachine.models.inventoryitems import InventoryItem

class InventoryService(InventoryInterface):
	inventoryDetails = {}

	def addItems(self,id,name,beverageId,stock,itemRequest):
		"""
		Adding items in inventory
		"""
		inventory = InventoryItem()
		inventory.setId(id)
		inventory.setName(name)
		inventory.setBeverageId(beverageId)
		inventory.setStock(stock)
		inventory.setItem(itemRequest)
		self.__class__.inventoryDetails[id] = inventory

		return inventory

	def removeItems(self,id):
		stock = InventoryItem[id].get('stock')
		stock -= 1
		return InventoryItem
