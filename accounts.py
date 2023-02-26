# task3 accounts.py
# author Marta Pacula
# searched for inspiration in google and chatGPT
# inspiration found: use string slicing and create a string of signs

number = input("Enter a 10-digit account number: ")
last_four = number[-4:]
hide_digits = "x"*6
masked_number = hide_digits + last_four
print (masked_number)