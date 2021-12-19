"""
Author: James ANthony Ortiz
File: functions.py
Description: Functions in Python
"""

import math
import urllib.request

#Exmaple of a function definition in python:

def sumcount(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

a = sumcount(100)
print(a)

#Obtaining the square root of a value:
x = math.sqrt(4)
res = 'The Sqrt of 4 is: {v}'.format(v=x)
print(res)

#Obtain html from web-address:
u = urllib.request.urlopen('http://www.python.org')
data = u.read() #read into a string
print(data) #print string


