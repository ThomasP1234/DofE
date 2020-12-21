# Global Variables and Scope
# ref: https://www.w3schools.com/python/
# Author: Thomas Preston

x = "awesome" # When this is commented out there is an error because the final print doesn't know what x is

def myfunc():
  x = "fantastic" # Where as when this is commented out, the global x is printed
  print("Python is " + x)

myfunc()

print("Python is " + x)

# You can add a variable to the global scope using the global keyword

def func():
    global y
    y = "super"
    print("Python is " + y)

func()

print ("Python is " + y)