# Multiple of 7
# num1 = int(input("Enter the number : "))
# if(num1%7==0):
#     print("Yes : ",num1)
# else:
#     print("NOt : ",num1)    



# string lengh condition
# str = input("Enter the string : ")
# if(len(str)<=10):
#     print("Sort : ")
# else:
#     print("Long : ")    

# str = input("Enter you name please : ")
# if(str[0]=="A"):
#     print("Nice Name :")
# else:
#     print("Cool Name :")    

# Mathematic calculation
# num1 = int(input("Enter first value : "))
# num2 = int(input("Enter second value : "))
# print("Addition : ",num1+num2)
# print("Multiplication : ",num1*num2)
# print("Divide : ",num1/num2)
# print("Modula :",num1%num2)
# print("Substraction : ",num1-num2)

# Password strength checker

# P = (input("Build you password : "))

# if(len(P)<8):
#     print("Password should be minumum 8 digit :")
# elif("a" in P or "b" in P or "c" in P or "d" in P)and ("1" in P or "2" in P or "3" in P or "4" in P):
#     print("strong password")
# else:
#     print("Week password")    

# Temprature cheaking 
# Tem = int(input("Enter Temprature : "))
# if Tem>=30:
#     print("Hot Weather ")
# elif(Tem>=15 and Tem<=25):
#     print("Nice/Moderate Temprature ")
# else:
#     print("Cool Temprature")


# Login system

# username = input("Enter username ")
# password = input("Enter password ")
# if username == "faizan_alam" and password == "9451357808":
#     print("Login Succesful :")
# else:
#     print("Try again : ")

# Take bill amount and number of persion, print how much pay single person

# bill = int(input("What's total bill : "))
# person = int(input("How much people? : "))
# store = bill/person
# print("Each person should pay: ",store)

# Grade Culculate

# marks = int(input("Enter marks : "))
# if marks>=90:
#     print("Grade A ")
# elif marks>=80 and marks<=89:
#     print("Grade B ")
# elif marks>=70 and marks<=79:
#     print("Grade C ")
# else:
#     print("Fail ")

# Rock paper scissor game

import random

user = input("Let's play ")
database = ['rock','paper','scissor']
Computer = random.choice(database)
print("Conputer ",Computer)
if user == Computer:
    print("Match Draw")
elif( user == "rock" and Computer == "scissor")or( user == "paper" and Computer == "rock")or( user == "scissor" and Computer == "paper" ):
    print(" You Win ")
else:
    print("Computer Win ")



# if user==store:
#     print(" Tie ")

# Username generator
# first_n = input("Enter First Name :")
# seco_n = input("Enter Second Name :")

# store =  first_n[0:3]
# store1 =  seco_n[0:3]

# username = store+store1
# print(username)