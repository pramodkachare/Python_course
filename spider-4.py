x = int(input('Enter a number'))

for i in range(x):
    if i%2:
        print(i, 'is Odd.')
    else:
        print(i, 'is Even.')
        
        
x = int(input('Enter a number'))


## Collect all even numbers
even = []
for i in range(x):
    if not i%2:
        print(i, 'is Even.')        
        even.append(i)
        
print('EVEN numbers: ', even)