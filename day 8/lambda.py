#example
"""def sum(a):
    return a+10

print(sum(10))"""

#same example in lambda
"""sum=lambda a:a+10

print(sum(10))"""

#doubler
"""def myFunc(n):
    return lambda a:a*n

doubler=myFunc(2)
triple=myFunc(3)
quadruple=myFunc(4)

print(doubler(10))
print(triple(10))
print(quadruple(10))"""

#Calculator
#Addition
#Subtraction
#Multiplication
#Division

print("The simple calculator which holds the features of addition, subtraction, multiplication and division:")
print("1:Addition")
print("2:Subtraction")
print("3:Multiplication")
print("4:Division")

operation = input("Enter a value")
if operation =="1":
    num1=input("enter the first number: ")
    num2=input("enter the second number: ")
    print("The sum of two number is " + str(int(num1) + int(num2)))

elif operation =="2":
    num1 = input("enter the first number: ")
    num2 = input("enter the second number: ")
    print("The differnce of two number is " + str(int(num1) - int(num2)))

elif operation =="3":
    num1 = input("enter the first number: ")
    num2 = input("enter the second number: ")
    print("The product of two number is " + str(int(num1) * int(num2)))

elif operation =="4":
    num1 = input("enter the first number: ")
    num2 = input("enter the second number: ")
    print("The quotient of two number is " + str(int(num1) / int(num2)))
    
else:
    print("it is invalid entry a calculator cannot calcualte")
