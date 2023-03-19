#collatz.py
#task4
#Author: Marta Pacula
#program asks for a positive number and run instructions 
#until the result is wqual 1 which stops the program

val = int(input("Enter a positive integer: "))
ans = val

while ans != 1:
    if (ans % 2) == 0:
        ans = ans / 2
    else:
        ans = (ans * 3) + 1
    print(f"The value is {ans}")