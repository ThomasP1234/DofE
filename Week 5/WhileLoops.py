# One of the primary loops in python
# ref: https://www.w3schools.com/python/
# Author: Thomas Preston

a = 1
while a < 10:
    print(a)
    a = a + 1 # Adds 1 to a each loop

b = 1
while b < 6:
  print(b)
  if b == 3:
    break
  b += 1

c = 0
while c < 6:
  c += 1
  if c == 3:
    continue
  print(c) # skips this step when c = 3

d = 1
while d < 10:
    print(d)
    d = d + 1
else:
    print('d is not long < 10')