#This is task 6
#Author Marta Pacula
#I checked Newton's estimation method but didn't understand much 
#Therefore I tried to find out by myself how to define a function and get the result even though, to do so,
# I needed to use math module


import math #import the module to be able to divide by suareroot


def root(number, number1):  #setting a function
    return number/number1

number = float(input("Please input a positive number ")) #asking for a float number
number1 = math.sqrt(number)
result = root(number, number1) #applying the function root()
rounded_result = round(result, 1) #getting a rounded result using the function round()
print(f"The suqreroot of {number} is approximately {rounded_result}")