x = 1
class Product:
    products = []
    def addProduct(self):
        userProducts = input("Please enter items to add separated by commas: ")
        productList = userProducts.split(",")
        for product in productList:
            self.products.append(product)
            print(f"{product} added to order")
class Inventory:
    inventory = {}
    def checkInventory(self):
        print(self.inventory)
    def removeItem(self):
        print(self.inventory)
        userChoice = input("Please enter the item you want to remove: ")
        if userChoice in self.inventory:
            self.inventory.pop(userChoice)
            print("Item removed :)")
        else:
            print("Item not in Inventory")

class Order:
    orderNum = 1
    orders = {}
    def confirmOrder(self):
        confirmation = input(f"Confirm order: {Product.products}? (Y/N) ")
        if confirmation == "Y":
            self.orders[self.orderNum] = Product.products
            for product in Product.products:
                if product in Inventory.inventory:
                    Inventory.inventory[product] += 1
                else:
                    Inventory.inventory[product] = 1
            Product.products.clear()

            self.orderNum += 1
        elif confirmation == "N":
            Product.products.clear()
    def reviewOrders(self):
        print(self.orders)

while x == 1:
    userInput = input("""Would you like to:
1. Add an order
2. Confirm an order
3. Check Current Inventory
4. Remove from Inventory
5. Review past orders
6. Exit
""")
    if userInput == "1":
        Product.addProduct(Product)
    elif userInput == "2":
        Order.confirmOrder(Order)
    elif userInput == "3":
        Inventory.checkInventory(Inventory)
    elif userInput == "4":
        Inventory.checkInventory(Inventory)
    elif userInput == "5":
        Order.reviewOrders(Order)
    elif userInput == "6":
        print("Thank you for shopping.")
        break