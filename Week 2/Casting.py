# Variables can be cast to specify the data type
# You can get the type of variable using the type function
# ref: https://www.w3schools.com/python/
# Author: Thomas Preston

n = 5
x = str(n)
y = int(n)
z = float(n)

print (x,y,z)

print("The value of x is" , x , ", and its type is: ", type(x))
print("The value of y is" , y , ", and its type is: ", type(y))
print("The value of z is" , z , ", and its type is: ", type(z))

# To join these together into a single string we have to cast the to type string
# We have to cast the type that aren't string already

print("The values of x, y and z are: " + x + ", " + str(y) + ", " + str(z))