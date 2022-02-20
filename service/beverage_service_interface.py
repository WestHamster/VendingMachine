import abc

class BeverageInterface(metaclass = abc.ABCMeta):
	@abc.abstractmethod

	def addBeverage(self,id,name,ingredients):
		pass
	def removeItems(self,id):
		pass