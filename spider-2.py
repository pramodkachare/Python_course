def add(a, b):
    return a + b

a1 = int(input('Enter number 1: '))
b1 = int(input('Enter number 2: '))

c = add(a1, b1)

def add(a, b):
    return a + b + 2

## Method-1
# import Utility as U
# print('Loaded from U.method()')
# U.add()
# U.subtract()

## Method-2
# from Utility import *
# print('Loaded directly')
# add()
# subtract()

## Method-3
from Utility import add, subtract, multiply, division
print(add(a1, b1))
print(subtract(a1, b1))
print(multiply(a1, b1))
print(division(a1, b1))