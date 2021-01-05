# Finding whether an expression is true or false
# Comparing 2 values and returning a boolean answer
# Printing a message based on whether its true or false
# Len function in classes
# Functions returning booleans
# Built-in functions that return booleans
# ref: https://www.w3schools.com/python/
# Author: Thomas Preston


print(5 > 4) # True
print(5 == 4) # False
print(5 < 4) # False


a = 14
b = 68

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a") # This is the outcome for these numbers


print(bool("Hello World")) # True
print(bool(45)) # True


print(bool("abcd"))
print(bool(987))
print(bool(["a","b","c"])) 
# All come back true


print(bool(False)) # False
print(bool(None)) # False
print(bool(0)) # False
print(bool("")) # All empty values come back false


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


def myFunction():
    return False # Change to true and it will return true

print(myFunction())


def newFunction():
    return True

if newFunction():
    print("Yes") # Doesn't have to print true or false - it can be whatever you want it to be
else:
    print("No")


x = 200
y = 25.3

print(isinstance(x, int))
print(isinstance(y, int))