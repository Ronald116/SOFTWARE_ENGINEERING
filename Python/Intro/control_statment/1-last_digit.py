#!/usr/bin/python3


import random
number = random.randint(-10000, 10000)
text = "Last digit of"

num = abs(number) % 10
if number < 0:
    num *= -1

if num > 5:
    print("{} is {} and is greater than 5".format(
        number, num))
elif num == 0:
    print("{} is {} and is zero".format(number, num))
elif num < 6 and num != 0:
    print("{} is {} and is less than 6 and not zero".format(number, num))
