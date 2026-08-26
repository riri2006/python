#-----------------------------------------CONDITIONAL STATEMENTS-------------------------------------

#q1
x = int(input("Enter the number : "))
if(x>0):
    print("Positive")
elif(x<0):
    print("Negative")
else:
    print("Zero")

#q2
print("QUESTION 06")
s = int(input("Enter a number: "))
if(s%2==0):
    print("Even")
else:
    print("Odd")

#q3
print("QUESTION 02")
age = int(input ("Enter your age: "))
if(age>=18):
    print("Eligible")
else:
    print("Not Eligible")

#q4
a = int(input("Enter 1st no.: "))
b = int(input("Enter 2nd no.: "))
c = int(input("Enter 3rd no.: "))
if(a>b and a> c):
    print(a, " is largest")
elif(b>a and b>c):
    print(b, " is largest")
else:
    print(c," is largest")

#q5
year = int(input("Enter year: "))
if(year%4==0 or (year%100==0 and year%400==0)):
    print("LEAP YEAR")
else:
    print("Not a leap year")

#----------------------------------------------FUNCTIONS--------------------------------------

#Q6
def greet():
    print("helloo python")

greet() #method1 of calling function
x = greet
x() #method 2
y = greet()
y #method 3

#q7

def greet(name):
    print("Hello ", name)

greet("David")

#q8
def add(x,y):
    print(x+y)

def call(fun,a,b):
    return fun(a,b)

x = call(add,10,3)

#q9
def func(num):
    if(num%2==0):
        return "EVEN"
    else:
        return "ODD"

print(func(5))

#q10
def largest(a,b,c):
    if(a>b and a>c):
        print(a , " is largest")
    elif(b>a and b>c):
        print(b, " is largest")
    else:
        print(c, " is largest")

largest(10,20,11)

#--------------------------------------------TRY EXCEPT-------------------------------------------

#Q11
def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("CANT DIVIDE BY ZERO")

div(10,2)
div(2,0)

#q12
try:
    a = int(input("Enter any integer: "))
except ValueError:
    print("ENTER ONLY INTEGER..")

#Q13
def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Cant divide by zero..")
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
except ValueError:
    print("Enter numeric values only")

div(a,b)

#----------------------------------------CLASSES AND OBJECTS--------------------------------------
#q16
class Car:
    def drive(self):
        print("Car is driving")

c1 = Car()
c1.drive()

#q17
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def S_name(self):
        print(self.name)

    def S_age(self):
        print(self.age)

s1= Student("Riddhi", 21)
s1.S_name()
s1.S_age()

#Q18
class Cars:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def C_brand(self):
        print("Brand:",self.brand)

    def C_model(self):
        print("Model:" ,self.model)

c1= Cars("Maruti Suzuki", "Swift")
c1.C_brand()
c1.C_model()

#q19
class Persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def P_name(self):
        print("Name:", self.name)
    def P_age(self):
        print("Age:", self.age)

p1 = Persons("Shilpa", 42)
p1.P_name()
p1.P_age()
p2 = Persons("Sharda", 42)
p2.P_name()
p2.P_age()
p3 = Persons("Riddhi", 21)
p3.P_name()
p3.P_age()

#q20:
class BankAccount:
    def __init__(self,name,amnt):
        self.name = name
        self.amnt = amnt
    def Holder_name(self):
        print("Holder name:", self.name)
    def Amount(self):
        print("Amount: ", self.amnt)

b1 = BankAccount("Riddhi" , 198900)
b1.Holder_name()
b1.Amount()

#---------------------------------------LEVEL 3-----------------------------------------------------
#-------------------------------------FUNC + OOPS----------------------------------------------------

#q21
class Calculator:
    def __init__(self, a, b):
        self.a= a
        self.b=b
    def add(self):
        print("Sum: ", self.a + self.b)
    def sub(self):
        print("Dufference: ",self.a - self.b)
    def mul(self):
        print("Product: ", self.a * self.b)
    def div(self):
        try:
            print("Division: ", self.a / self.b)
        except ZeroDivisionError:
            print("Cant divide by 0")

c1 = Calculator(10,20)
c1.add()
c1.sub()
c1.mul()
c1.div()
c2 = Calculator(10,0)
c2.div()

#Q22
class  Car:
    def C_brand(self, brand):
        self.brand = brand
    def C_Model(self, model):
        self.model=model
    def year(self,y):
        self.y=y
    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year: ",self.y)

c1 = Car()
c1.C_brand("Maruti Suzuki")
c1.C_Model("Swift")
c1.year(2016)
c1.display_info()

#q23
class Student:
    def S_name(self,name):
        self.name = name
        print(self.name)
    def marks(self,mrk):
        self.mrk=mrk
    def result(self):
        if(self.mrk>=40):
            print("PASS")
        else:
            print("FAIL")

s1 = Student()
s1.S_name("Riddhi")
s1.marks(98)
s1.result()

#q24
class BankAccount:
    def __init__(self,balance):
        self.balance= balance
    def deposit(self,amount):
        self.amount=amount
        print("Deposited ", self.amount , " Succesfully")
        self.balance = self.balance + self.amount
    def withdraw(self,withdraw_amnt):
        self.withdraw_amnt= withdraw_amnt
        if(self.balance>=self.withdraw_amnt):
            print("withdrawn ", self.withdraw_amnt , "successfully")
            self.balance = self.balance- self.withdraw_amnt
        else:
            print("INSUFFICIENT BALANCE...")
    def show_balance(self):
        print("BALANCE: " , self.balance)

account1= BankAccount(10000)
account1.deposit(5000)
account1.withdraw(15000)
account1.show_balance()

# ---------------------------------------------LEVEL 4------------------------------------------------------------
#------------------------------------------------INHERITANCE-------------------------------------------------
#26
class Animal:
    def eat(self):
        print("Eating..")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()

#27
class Animal:
    def eat(self):
        print("Eating..")
    def sleep(self):
        print("Sleeping..")

class Dog(Animal):
    def bark(self):
        print("Barking..")

doggy = Dog()
doggy.eat()
doggy.sleep()
doggy.bark()

#28
class Car:
    def __init__(self,br,mo):
        self.br = br
        self.mo = mo
    def brand(self):
        print("Brand:", self.br)
    def model(self):
        print("Model:", self.mo)

class ElectricCar(Car):
    def E_battery(self,battery):
        self.battery= battery
        print("Battery:", self.battery)

e1 = ElectricCar("ABC", "ab12")
e1.brand()
e1.model()
e1.E_battery(1234)

#29
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def P_name(self):
        print("Name:", self.name)
    def P_age(self):
        print("Age:", self.age)

class Student(Person):
    def course(self, c):
        self.c = c
        print("Course:", self.c)

s1 = Student("Riddhi", 21)
s1.P_name()
s1.P_age()
s1.course("Python")

#30
class Animal:
    def first(self):
        print("Parent class")

class Dog(Animal):
    def second(self):
        print("Child class 1")

class Puppy(Dog):
    def third(self):
        print("Child class of child class 1")

p1 = Puppy()
p1.first()
p1.second()
p1.third()

#-------------------------------------------------------------LEVEL 5-----------------------------------------------
#-----------------------------------------------------------SUPER---------------------------------------------------

#31
class Car:
    def __init__(self,br):
        self.br = br
  
class ElectricCar(Car):
    def __init__(self,br,battery):
        super().__init__(br)
        self.battery=battery
        
    def Display(self):
        print("Brand:", self.br)
        print("Battery:", self.battery)

e1 = ElectricCar("ABC", "123")
e1.Display()

#32
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age, course):
        super().__init__(name,age)
        self.course=course
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

s1 = Student("Riddhi", 21, "python")
s1.display()

#33
class Car:
    def start(self):
        print("Car is starting..")
  
class ElectricCar(Car):
    def start(self):
        super().start()
        print("E car is starting..")

e1 = ElectricCar()
e1.start()


#34
class Animal:
    def speak(self):
        print("parent class is speaking")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Child class is speaking")

doggy = Dog()
doggy.speak()

#35
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
class Car(Vehicle):
    def __init__(self, brand,model,color):
        super().__init__(brand,model)
        self.color=color
    def display(self):
        print("Brand:",self.brand)
        print("Model:", self.model)
        print("Color:",self.color)
v1= Car("Maruti Suzuki", "Swift", "White")
v1.display()


