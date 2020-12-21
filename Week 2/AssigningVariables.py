# Assigning Many Values to Multiple Variables
# Assigning One Value to Multiple Variables
# Unpacking a list
# ref: https://www.w3schools.com/python/
# Author: Thomas Preston

x, y, z = 1, 2, 3

print(x)
print(y)
print(z)

print() # New line in output

x = y = z = 4 # This x, y, z overrides the previous giving it a new value

print(x)
print(y)
print(z)

print()

fruits = ["apple", "orange", "banana"]
x, y, z = fruits

print(x)
print(y)
print(z)