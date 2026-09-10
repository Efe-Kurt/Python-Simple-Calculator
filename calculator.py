# Version 1.1 - Updated via Terminal

print("\n\nWe are gonna do a simple calculator today.")
print("İt's going to do addition,subtraction,multiplication,divison\n\n")

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number"))

action = int(input("Enter an action(add=1,sub=2,mult=3,div=4):"))

if(action == 1):
    print(num1 + num2)
elif(action == 2):
    if(num1 > num2):
        print(num1 - num2)
    else:
        print(num2 - num1)
elif(action == 3):
    print(num1*num2)
elif(action ==4):
    if(num2 == 0):
        print("\nCan not be divided by zero")
    else:
        print(num1/num2)
        print("remaining:",num1%num2)

   
    print("\n\n\n")
