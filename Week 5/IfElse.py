# If, elif and else statements
# ref: https://www.w3schools.com/python/
# Author: Thomas Preston


# If
a = 25
b = 14
if a > b:
    print('a is greater than b') # This indentation is very important



# If, Elif
a = 12
b = 12
if a > b:
    print(' a is greater than b')
elif a == b:
    print('a and b are equal')



# If, Elif, Else
a = 22
b = 35
if a > b:
    print(' a is greater than b')
elif a == b:
    print('a and b are equal')
else:
    print('a is smaller than b')



# If, Else
a = 25
b = 34
if a > b:
    print(' a is greater than b')
else:
    print('a is not greater than b')



# Shorthand If
a = 20
b = 31
if a > b: print(' a is greater than b')

# Shorthand If, Else
a = 5
b = 210
print('A') if a > b else print ('B')

# Shorthand multiple else statements
a = b = 20
print('A') if a > b else print ('=') if a == b else print ('B')

# Multiple conditions (AND)
a = 5
b = 10
c = 10
if a < b and b == c:
    print('a<b=c')

# Multiple conditions (OR)
a = 20
b = 15
c = 15
if a < b or b == c:
    print('one condition is true')

# Nested if statements
a = 15
if a > 10:
    print('A is greater than 10')
    if a > 20:
        print('A is greater than 20')
    else:
        print('But not greater than 20')

# Pass statement
a= 20
if a > 10:
    pass # Cannot have an empty if statement so putting pass in it acts like its empty

