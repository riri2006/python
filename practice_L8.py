#-----------------------------------------------------LEVEL 8---------------------------------------------------
#1
class Car:
    def __init__(self,brand, model):
        self.brand=brand
        self.model = model
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
class ElectricCar(Car):
    def __init__(self,brand, model, color):
        super().__init__(brand,model)
        self.color=color
    def display(self):
        super().display()
        print("Color:", self.color)
    
e1 = ElectricCar("ABC","xyz","black")
e1.display()

#2
class Animals:
    def __init__(self, n):
        self.name = n
    def eat(self):
        print(self.name,"is eating")
class Dog(Animals):
    def __init__(self, n, breed):
        super().__init__(n)
        self.breed = breed
    def eat(self):
        super().eat()
        print(self.name,"is of", self.breed, "breed and it is eating its food")
puppy = Dog("Shiro","pomerian")
puppy.eat()

#3
class Bankaccount:
    def __init__(self,balance):
        self.__balance = balance
        # print("Balance:", self.__balance)

    def Deposit(self,amnt):
        self.deposit=amnt
        print("Deposited",self.deposit,"successfully..")
        self.__balance = self.__balance + self.deposit
    def Withdraw(self,withdraw_amount):
        self.withdraw = withdraw_amount
        if(self.__balance>= withdraw_amount):
            print("Withdrawn", self.withdraw,"Successfully..")
            self.__balance -= withdraw_amount
        else:
            print("INSUFFICIENT BALANCE")
    def getbalance(self):
        return self.__balance

a1 = Bankaccount(10000)
a1.Deposit(5000)
a1.Withdraw(15000)
print("Current Balance:",a1.getbalance())
# print(a1.__balance)


#4
class Food:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("GOOD FOOD = GOOD MOOD")
        
class Fruits(Food):
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color
    def eat(self):
        super().eat()
        print("Fruits are beneficial for health..")
    def taste(self):
        print("Fruits are sweet in taste...")

class Mango(Fruits):
    def __init__(self,name,color, season):
        super().__init__(name,color)
        self.season = season
    def Info(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Season:", self.season)
    def taste(self):
        super().taste()
        print(self.name, "is Sweet and Tangy in taste")

class Lychee(Fruits):
    def __init__(self,name,color, season):
        super().__init__(name,color)
        self.season = season
    def Info(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Season:", self.season)
    def taste(self):
        super().taste()
        print(self.name, "is Sweet and juicy in taste")

print()
fruit = Fruits("Fruitsss","Colorrrrr")
fruit.eat()
print()

mango = Mango("Alphonso Mango","Yellow","Summer")
mango.Info()
mango.taste()
print()
print()

lychee = Lychee("Lychee","Pinkish","Summer")
lychee.Info()
lychee.taste()