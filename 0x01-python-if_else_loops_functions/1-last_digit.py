#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
str1 = "Last digit of {} is -{} and is less than 6 and not 0"
str2 = "Last digit of {} is {} and is greater than 5"
str3 = "Last digit of {} is {} and is less than 6 and not 0"
if number < 0:
    print(str1.format(number, last))
elif number > 0:
    if last > 5:
        print(str2.format(number, last))
    elif last == 0:
        print("Last digit of {} is {} and is 0".format(number, last))
    else:
        print(str3.format(number, last))
