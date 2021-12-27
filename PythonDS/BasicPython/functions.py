#
# Author: James Ortiz
# File: functions.py
# Description: Functions in Python 3
#
#

def square(n):
    return n ** 2

print(square(4))

print('Using Newtons Square Root Approximation Algorithm: ')
def square_root(n):
    root = n / 2 #Initial guess with be 1/2 of n
    for k in range(20):
        root = (1/2) * (root + (n / root))
    return root

print('Square root in Newtons method: ', square_root(4563))



    
