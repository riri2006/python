def greet():
    print("Hello!")

call = greet
call()


def student():
    print("This is student")

def call(func):
    func()

abc = call
abc(student)

def mult(a,b):
    return a*b

def call(fun,x,y):
    return fun(x,y)

result = call(mult,10,2)
print(result)


def mult(a,b):
    print("product: ", a*b)

def call(fun,x,y):
    return(fun(x,y))

result = call(mult,10,2)
result



class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("hello")    


def add(calc: Calculator):
    print(calc.a + calc.b)


c1 = Calculator(10, 20)

add(c1)



def outer():
    def inner():
        print("Inner function")

    return inner

my_function = outer()
my_function()