#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
digit = abs(number) % 10
digit =  digit
if digit > 5:
    print(f'Last digit of:{number:d} is {digit}and is greater than 5')
elif digit == 0:
    print(f'Last digit of:{number:d} is {digit}and is 0')
else:    
    print(f'Last digit of:{number:d} is {digit} and is less than 6 and not 0')
