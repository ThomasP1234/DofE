# You can get python to return only certain characters from a string
# ref: https://www.w3schools.com/python/
# Author: Thomas Preston

a = "Hello World!"
print (a[3:8]) # From 3-8 - prints 'lo Wo'
print (a[:5]) # From start to 5 - prints 'Hello'
print (a[6:]) # From 6 to end - prints 'World!'

print (a[6:][:5]) # From 6 to end and from that the start to 5 - prints 'World'

print(a[-5:-2])