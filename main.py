class computer:
    def __init__(self):
        self.__maxprice = 700
    def sell(self):
        print("selling price :", self.__maxprice)
    def setprice(self,price):
        self.__maxprice = price

#object creation
obj = computer()
obj.sell()

obj.__maxprice = 2000
obj.sell()

obj.setprice(2500)
obj.sell()