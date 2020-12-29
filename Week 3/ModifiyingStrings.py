# You can change the string with some simple commands
# ref: https://www.w3schools.com/python/
# Author: Thomas Preston

a = 'Hello World'
print(a.upper()) # print it all in upper case ('HELLO WORLD')
print(a.lower()) # prints it all in lower case ('hello world)

b = '   Hello World   '
print(b.strip()) # removes unneccessary spaces from the string(whitespace) ('Hello World')
print(b.strip().upper()) # All caps and no whitespace
print(b.replace("o", ".")) # You can replace charcters with other characters in the string

c = 'Hello, World'
print(c.split(",")) # Splits it at the comma and splits it into a list
print(c.replace(',','').split(" ")) # removes the comma and splits it into a list