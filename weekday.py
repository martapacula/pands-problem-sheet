#Task 5
#weekday
#research on #geeksforgeeks.org #pynative.com #stackoverflow.com

import datetime #import statement to import built-in module datetime and use its functions

today = datetime.date(2023, 3, 25)

day_of_week = today.weekday() #using weekday function 
#to get the day of the week as an integer (where Monday is 0 and Sunday is 6)

if day_of_week < 5:
    print("Today is a weekday")
else:
    print("Yay, it's the weekend")