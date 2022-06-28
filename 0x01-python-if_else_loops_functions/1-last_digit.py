#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = int(number)
if number < 0:
    last_num = last_num % -10
else:
    last_num = last_num % 10
if last_num > 5:
    print(f"Last digit of {number:d} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number:d} is {last_num} and is 0")
else:
    print(f"Last digit of {number:d} is {last_num} and less than 6 and not 0")
