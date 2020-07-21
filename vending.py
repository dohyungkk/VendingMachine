import sys

price_unit = 0.50

class texts:
    title = "Thanks for using %s vending machine!"
    product = "%s:%s ($ %s)"
    insert_coin = "Please pay me with coins\n"
    not_enough_coin = "Need more coins! \n Change is $ %s."
    select_product = "Choose the drink you want\n"
    select_wrong = "Sorry, we don't have that drink\n"
    product_out = "You chose %s. Change is $ %s. \n Thank you for using us!"

class Product:
    #Easy way to access Product and Price
    productType = {"1": "Water", "2": "Pop", "3": "Coffee"}
    productValue = {"1": "1.00", "2": "1.50", "3": "2.00"}

class CoffeeVM(Product):
    _name = "Coffee"

    def __init__(self):
        #prints _name when chosen which VM to use
        print(texts.title %self._name)

    def run(self):
        while True:
            try:
                inputCoin = float(input(texts.insert_coin))
            except ValueError:
                #prints error when user chooses wrong type
                print(texts.select_wrong)
            else:
                self.selectProduct(inputCoin)
    
    def selectProduct(self, coin):
        description = ""
        for selection, item in Product.productType.items():
            price = self.getProductValue(selection)
            description += selection + ":" + item + "($" + str(price) + ")"

        print(description)
        inputProduct = input(texts.select_product)
        productValue = self.getProductValue(inputProduct)

        if productValue:
            productName = self.getProductName(inputProduct)
            self.payment(coin, productName, productValue)

        else:
            print(texts.select_wrong)
            self.selectProduct(coin)

    def getProductValue(self, product):
        returnValue = 0
        for selection, value in Product.productValue.items():
            if selection == product:
                returnValue = value
        return returnValue

    def getProductName(self, product):
        for selection, name in Product.productType.items():
            if selection == product:
                return name

    def payment(self, coin, name, value):
        coinValue = coin * price_unit
        coinValue = float(coinValue)
        value = float(value)
        if coinValue >= value:
            balance = coinValue - value
            print(texts.product_out % (name, int(balance)))
        else:
            print(texts.not_enough_coin % int(coinValue))
        #Goes back to the main menu
        self.run()

#SnackVM inherits CoffeeVM
class SnackVM(CoffeeVM):
    _name = "Snacks"

    def __init__(self):
        #Overriding Product and Price
        Product.productType = {"1": "Candy", "2": "Chocolate", "3": "Chips"}
        Product.productValue = {"1": "1.00", "2": "1.75", "3": "2.50"}
        print( texts.title % self._name)

if __name__ == "__main__":
    print("1: Drink, 2: Snack")
    select_vm = input("Choose the vending machine you want.\n").strip()

    if select_vm == "1":
        vm = CoffeeVM()

    elif select_vm == "2":
        vm = SnackVM()
    
    else:
        print("Sorry, we don't have that VM! Please choose again.\n")
        sys.exit(-1)

    try:
        vm.run()

    except KeyboardInterrupt as exc:
        print("Closing VM!")