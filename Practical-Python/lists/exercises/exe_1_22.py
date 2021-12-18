"""
Author: James Anthony Ortiz
File: exe_1_21.py
Description: Membership tests
"""

symlist = ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']

#Useing the append() method to add a symbol to list:

symlist.append('RHT')
print('List with RHT appended: ' + symlist)

#Insert 'AA' as the second item in the list:
symlist.insert('AA', 1)
print('List with aa inserted as the second item: ' + symlist)

#Remove 'MSFT' from the list:
print('Original list: ' + symlist)
symlist.remove('MSFT')
print('List with MSFT omitted: ' + symlist)

#Append 'YHOO' at the end of the list:
print('Original List: ' + symlist)
symlist.append('YHOO')
print('Modified list: ' + symlist)

#Count how many times 'YHOO' is in the list:
print('The amount of times YHOO is in the list: ' + symlist.count('YHOO'))


