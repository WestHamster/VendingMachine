import abc

class InventoryInterface(metaclass = abc.ABCMeta):
	@abc.abstractmethod

	def addItems(self,id,name,beverageId,stock,itemRequest):
		pass
	def removeItems(self,id):
		pass