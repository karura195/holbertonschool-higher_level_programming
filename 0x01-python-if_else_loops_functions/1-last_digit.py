#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of {} is -{} and is less than 6 and not 0"
str2 = "Last digit of {} is {} and is greater than 5"
str3 = "Last digit of {} is {} and is less than 6 and not 0"
if number < 0:
    n = -number
    last = n % 10
    print(str1.format(number, last))
elif number > 0:
    last = number % 10
    if last > 5:
        print(str2.format(number, last))
    elif last == 0:
        print("Last digit of {} is {} and is 0".format(number, last))
    else:
        print(str3.format(number, last))
else:
    print("Last digit of 0 is 0 and is 0")
