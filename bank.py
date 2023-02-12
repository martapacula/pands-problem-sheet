# bank.py 
# Author: Marta Pacula
# program prints out the sum in euro of two amounts given in cents


x = int(input("Enter amount1(in cents): "))
y = int(input("Enter amount2(in cents): "))
ans = (x+y)/100
print(f"The sum of these is €{ans}")
