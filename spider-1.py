a = [1, 2, 3, 4, 5]

print(a, type(a))


b = [10, 20, 30, 40, 50]

d = 'Pramod'

print('addition of a[0] and b[0]', a[0]+b[0])
print('subtration of a[0] and b[0]', a[0]-b[0])
print('miltiplication of a[0] and b[0]', a[0]*b[0])
print('division of a[0] and b[0]', a[0]/b[0])

def add(a, b):
    c = a + b
    return c

print('addition of 12 and 15 is ', add(12, 15))

for num in range(14):
    print(num)
    
import numpy as np    

print()