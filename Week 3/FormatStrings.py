# In python strings and numbers cannot be combined but format() can be used to combine them
# ref: https://www.w3schools.com/python/
# Author: Thomas Preston

age = 23
txt = "My name is Tim and I am {}"
print(txt.format(age))

# format() can take an unlimited number of argument the example above used 1 but bellow uses 3

price = 50
itemno = 200
quantity = 5
myorder = "I want {0} peices of item {1} and I will pay {2} pounds"
print(myorder.format(quantity, itemno, price))
                    #   0        1       2