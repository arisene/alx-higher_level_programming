#!/usr/bin/python3
import random
number = random.randint(-10, 10)

for i in range(4):

    num = int(number)
    if num>0:
        print("is positive")
    elif num<0:
        print("is negative")

    elif num==0:
        print("is zero")
    


