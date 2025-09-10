# Not a real infinite loop
# for i in range(10**100):
#   print(i)

# Real infinite loop
from itertools import count
for i in count():
    print("Value of i: ", i)
