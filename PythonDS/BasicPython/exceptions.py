#
# Author: James Ortiz
# File: exceptions.py
# Description: Exceptions in Python
#

import math #importing the math class, to use in program

a_number = int(input("Please enter an integer: "))
try:
    print(math.sqrt(a_number))
except:
    print("Bad value for square root.")
    print("Using absolute value instead")
    print(math.sqrt(abs(a_number)))
    
print('Demo #2:')
a_num_2 = int(input('Please enter an integer: '))
if a_num_2 < 0:
    raise RuntimeError("You cant use a negative number.")
else:
    print(math.sqrt(a_num_2))

    