# Main driver function

# API end-points:
#
# 1. Display all beverage
# 2. Dispensing different types of beverage
# 3. Adding to inventory, altering if inventory is short
import time
from datetime import datetime
import json
import sys
# append the path where file is present. Use pwd command if using Linux, else use 'cd'
sys.path.append('/Users/ankuranand/Desktop/LLD/')


from VendingMachine.controller.inventory_controller import InventoryController
from VendingMachine.controller.beverage_controller import BeverageController
from VendingMachine.controller.ingredient_controller import IngredientController

from VendingMachine.service.inventory_service import InventoryService
from VendingMachine.service.beverage_service import BeverageService
from VendingMachine.service.ingredient_service import IngredientService


ingredientController = IngredientController(IngredientService())
beverageController = BeverageController(BeverageService())
inventoryController = InventoryController(InventoryService())


ingredient1 = ingredientController.addIngredient('ing1','tea',40)
ingredient2 = ingredientController.addIngredient('ing2','milk',30)
ingredient3 = ingredientController.addIngredient('ing3','water',40)
ingredient4 = ingredientController.addIngredient('ing4','sprite',10)
ingredient5 = ingredientController.addIngredient('ing5','coffee',10)
ingredient6 = ingredientController.addIngredient('ing6','coca-cola',5)
ingredient7 = ingredientController.addIngredient('ing7','sugar',15)

# Default stock value
stock = {"water":40,"tea":40,"milk":30,"sprite":10,"coffee":10,"coca-cola":5,"sugar":15}

inventory = inventoryController.addItems('inventory1','',100,stock,[])



def breakRequest(payload):
	"""
	Taking input from client
	"""
	#payload = json.loads(client_input)
	beverage = payload['beverage']
	req_ingredients = payload['ingredient_with_quant']
	# print(beverage)
	ingredients = {}
	for items in req_ingredients:
		ingredients = items
	# print(ingredients)
	inventory = inventoryController.addItems('inventory1',beverage,100,stock,ingredients)
	balance = inventoryController.getIngredientBalance('ing1')
	if not balance:
		return False
	return True

def printInventory(inventory):
	"""
	Display inventory items
	"""
	print("\n",inventory.stock)


def checkIfEmpty(inventory):
	"""
	Keep checking if empty or not
	"""
	stock_val = inventory.stock
	if 0 in stock_val.values():
		print(stock_val)
		print("\n\nSome stock needs to be refilled!!\n\n")



_now = datetime.now()
current_time = _now.strftime("%HH")

if __name__ == '__main__':
    # should be in form of executing localhost:/

    if current_time < '12H':
        print("Good Morning")
    elif current_time < '16H':
        print("Good Afternoon")
    elif '3H' > current_time > '22H':
        print("Late evenings!")
    else:
        print("Good Evening")
    print()
    print()
    print("To exit press Ctrl-C")
    print()
    try:
        while 5:
            print()
            print()
            print("Starting Server...\n")
            time.sleep(1)
            print("Select an option:\n")
            checkIfEmpty(inventory)
            print("\t1. Order items.\n\t2. Display Inventory.\n\t3. To exit, press 0.\n\t")
            client_input = int(input())
            if client_input == 1:
                print()
                print('127.0.0.1:8000/orderItems')
                print()
                time.sleep(1)
                client_input = input("Enter the input in following format:\n{\"beverage\":\"name_of_beverage\",\"ingredient_with_quant\":[{\"ingredient1\":0,\"ingredient1\":0,\"ingredient1\":0}]}\n\n\n")
                # dumping string to make it in JSON formatted input
                client_json = json.loads(client_input)
                process_req = breakRequest(client_json)
                if not process_req:
                	print("\n\nSorry short of items currently!!")
                else:
                	print("\n\nYour order is served!")
                print("\n\nHope you had a good time!")
                time.sleep(1)
                print()
            elif client_input == 2:
                print()
                print('127.0.0.1:8000/InventoryDetails')
                print("\n\nInventory Details:")
                printInventory(inventory)
                time.sleep(1)
                # repsonse = placeOrder()
                print()
            elif client_input == 0:
                print()
                print("Thank you for your time")
                break
            else:
                print("Invalid Input")
            time.sleep(3)
    except KeyboardInterrupt:
        print()
        print("Hope you had a good time!")



# Basic code allocation

# ingredient1 = ingredientController.addIngredient('ing1','tea',2)
# ingredient2 = ingredientController.addIngredient('ing2','milk',2)
# ingredient3 = ingredientController.addIngredient('ing3','water',1)

# ingredients = [ingredient1,ingredient2,ingredient3]
# beverage1 = beverageController.addBeverage('beverage1','tea',ingredients)


# stock = {"water":3,"tea":4,"milk":3}
# itemsRequested = {"coffee":2, "milk":2,"water":1}

# inventory1 = inventoryController.addItems('inventory1','beverage1',100,stock,itemsRequested)

# balance = inventoryController.getIngredientBalance('ing1')
# print(balance)

# print("Ingredients:",beverage1.getIngredient())
# print("Inventory items:", inventory1.getStock())

























