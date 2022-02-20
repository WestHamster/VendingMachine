import abc

class IngredientInterface(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def addIngredient(self,id,name,quantity):
		pass