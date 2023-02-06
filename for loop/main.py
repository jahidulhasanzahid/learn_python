# for loop = a statement that will execute it's block for a limited amount of time
# for loop is limited time
# while loop is unlimited

# for index in range(10):
#     print(index+1)

# range(x, y) x is starting point which is inclusive and y is second number which is exclusive
# for index in range(50, 100+1):
#     print(index)

# range(x,y,z)
# for index in range(50, 100+1,2):
#     print(index)

# for index in "Jahidul Hasan":
#     print(index)

import time


for index in range(10, 0, -1):
    print(index)
    time.sleep(1)
print(index)
print("Happy New Year!")