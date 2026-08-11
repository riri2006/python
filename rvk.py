#Questions:

#1
print("QUESTION 01")
x = int(input("Enter the number : "))
if(x>0):
    print("Positive")
elif(x<0):
    print("Negative")
else:
    print("Zero")

#2
print("QUESTION 02")
age = int(input ("Enter your age: "))
if(age>=18):
    print("Eligible")
else:
    print("Not Eligible")

#3
print("QUESTION 03")
r = int(input("Enter the first number : "))
v = int(input("Enter the second number : "))

if(r>v):
    print("First is greater..")
elif(v>r):
    print("Second is greater..")
else:
    print("Both are equal..")

#4
print("QUESTION 04")
marks = int(input("Enter the marks : " ))
if(marks>=40):
    print("Pass")
else:
    print("Fail")

#5
print("QUESTION 05")
mrks = int(input("Enter the marks : "))
if(mrks >= 90 and mrks < 100):
    print("Grade A")
elif(mrks >= 80 and mrks < 90):
    print("Grade B")
elif(mrks >= 70 and mrks < 80):
    print("Grade C")
elif(mrks >= 60 and mrks < 70):
    print("Grade D")
else:
    print("FAIL")

#6
print("QUESTION 06")
s = int(input("Enter a number: "))
if(s%2==0):
    print("Even")
else:
    print("Odd")

#7
print("QUESTION 07")
j = 25
if(type(j)==int):
    print("Integer")
elif(type(j)==float):
    print("Float")
else:
    print("String")

#8
print("QUESTION 08")
temp=float(input("Enter temperature: "))
if(temp>40):
    print("Very Hot")
elif(temp>=30 and temp <=40):
    print("Hot")
elif(temp>=20 and temp<30):
    print("Normal")
else:
    print("Cold")

#9
print("QUESTION 09")
username = "admin"
age = 20

if(username=="admin"):
    if(age>=18):
        print("ACCESS GRANTED")
    else:
        print("Age Restriction")
else:
    print("Invalid user")

#10
print("QUESTION 10")
a=10
b=5
op = "+"

if(op=="+"):
    print(a+b)
elif(op=="-"):
    print(a-b)
elif(op=="*"):
    print(a*b)
else:
    print(a/b)

#11
print("QUESTION 11")
balance = int(input("Enter balance: "))
withdraw= int(input("Enter winthdrawal : "))
pin= 1234
entered_pin = int(input("Enter PIN : "))

if(pin != entered_pin):
    print("INVALID PIN !! ")
else:
    if(withdraw>balance):
        print("INSUFFICIENT BALANCE..")
    else:
        if(withdraw > 0):
            print("WITHDRAWAL SUCCESSFUL")
        else:
            ("INVALID AMOUNT")

#12
print("QUESTION 12")
m= int(input("Enter Marks: "))
age = int(input("Enter age :"))
ent_exam = int(input("enter entrance exam score : "))

if(age<18):
    print("NOT ELIGIBLE..")
else:
    if(marks>=80):
        if(ent_exam >= 70 ):
            print("Admission Granted..")
        else:
            print("Enterance score too loww... ")
    else:
        print("Academic score too low..")


