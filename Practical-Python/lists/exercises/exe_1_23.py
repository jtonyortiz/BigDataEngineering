"""
Author: James Anthony Ortiz
File: exe_1_23.py
Description: Sorting with Lists
"""

#Sorting a list with sort()
symlist = ['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
print('Original List: ' )
print(symlist)
symlist.sort()
print('Sorted List: ')
print(symlist)

#Sorting in reverse
symlist.sort(reverse=True)
print('Sorting in reverse: ')
print(symlist)


