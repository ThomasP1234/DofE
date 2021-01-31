# Classes in python
# ref: https://www.w3schools.com/python/
# Author: Thomas Preston

class MyClass:
    x = 10

obj = MyClass()
print(obj.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Joe", 21)

print(p1.name)
print(p1.age)

