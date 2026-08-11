# import numpy as np

# #question 1
# def division(a,b):
#     try:
#         print("division: ", a/b)
#     except ZeroDivisionError:
#         print("Cant divide by zero..")

# try:
#     x= int(input("Enter the first number: "))
#     y= int(input("Enter the second number: "))
#     division(x,y)
# except ValueError:
#     print("Invalid values..")

# #question2
# def check_age(age):
#     if(age>= 18):
#         print("Eligible")
#     else:
#         print("Not Eligible")

# try:
#     a = int(input("Enter your age: "))
#     check_age(a)
# except ValueError:
#     print("Invalid value..")

# #question3
# def calculator( a,b,op):
#     if(op=="+"):
#         print("sum: ", a+b)
#     elif(op=="-"):
#         print("difference: ", a-b)
#     elif(op=="*"):
#         print("product: ", a*b)
#     elif(op=="/"):
#         try:
#             print("division:" , a/b)
#         except ZeroDivisionError:
#             print("Cant divide by zerooo..")
#     else:
#         print("INVALID OPERATOR")

# try:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))
#     op=input("Enter the operator: ")
#     calculator(a,b,op)
# except ValueError:
#     print("Enter numbers only..")

# #question4
# def grade(mrks):
#     if(mrks>100 or mrks<0):
#         print("Please enter valid marks..")
#     else:
#         if(mrks >= 90 and mrks < 100):
#             print("Grade A")
#         elif(mrks >= 80 and mrks < 90):
#             print("Grade B")
#         elif(mrks >= 70 and mrks < 80):
#             print("Grade C")
#         elif(mrks >= 60 and mrks < 70):
#             print("Grade D")
#         else:
#             print("FAIL")

# try:
#     marks= int(input("Enter your marks: "))
#     grade(marks)
# except ValueError:
#     print("PLEASE ENTER MARKS IN NUMBERS ONLY")


# #QUESTION5
# def id_card(name, age, roll):
#     print("Student Name: ", name)
#     print("Student Age: ", age)
#     print("Student roll no. ", roll)

# try:
#     name= str(input("Enter name: "))
# except NameError:
#     print("do not use any numeric value")
# try:
#     age= int(input(""))


def calculator(*num, op):
    if(op=="+"):
        print(sum(num))
    elif(op=="-"):
        print()
    elif(op=="*"):
        print("product: ", a*b)
    elif(op=="/"):
        try:
            print("division:" , a/b)
        except ZeroDivisionError:
            print("Cant divide by zerooo..")
    else:
        print("INVALID OPERATOR")

try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    op=input("Enter the operator: ")
    calculator(a,b,op)
except ValueError:
    print("Enter numbers only..")







        











