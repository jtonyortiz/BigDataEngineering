#
# Author: James Ortiz
# File: string_formatting.py
# Description: String formatting in python
#

print('Hello')
print('Hello', 'World')
print('Hello', 'World', sep='***')
print('Hello', 'World', end="***")
print()
print('Hello', end="***") 
print('World')

#Output Formatting
name = 'James'
age = '30'
print(name, 'is', age, ' years old')

price = 24
item = 'banana'
print('The %s costs %d cents' % (item,price))
print('The %+10s costs %5.2f cents' % (item, price))
print('The%+10s costs %10.2f cents' % (item, price))
item_dict = {"item": "banana", "cost": 24}
print("The %(item)s costs %(cost)7.1f cents" % item_dict)

