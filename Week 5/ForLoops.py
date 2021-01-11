# One of the primary loops in python
# ref: https://www.w3schools.com/python/
# Author: Thomas Preston


mylist = ["1","2","3"] # Usually prints as [1,2,3]
for x in mylist:
    print(x) # Prints each item in the list one at a time

for x in 'Hello World':
    print(x) # Prints each letter at a time



# Break after 3
mylist = ["1","2","3","4"] 
for x in mylist:
    print(x)
    if x == "3":
        break

# Break before 3
mylist = ["1","2","3","4"] 
for x in mylist:
    if x == "3":
        break
    print(x)


# Continue
mylist = ["1","2","3","4"] 
for x in mylist:
    if x == "3":
        continue
    print(x)


# Range
for x in range(10): # Print 0-9
    print(x)

for x in range(2, 10): # Prints 2-9
    print(x)

for x in range(2, 10, 2): # Prints 2-9 in increments of 2 (eg. 2, 4, 6, 8)
    print(x)



# Else in for loop
mylist = ["1","2","3"]
for x in mylist:
    print(x)
else:
    print('Done')



# Nested loops
adj = ["Red", "Green", "Blue"]
obj = ["Chair", "Desk", "Phone"]
for x in adj:
    for y in obj:
        print(x, y)



# Pass
for x in [1, 2, 3]:
    pass