"""
Author: James Anthony Ortiz
File: exe_1_19.py
Description: Extracting and reassigning list elements
"""

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
print('Initial List: ' + symbols)

#Split the list into names:
symlist = symbols.split(',')
print('Splitting list: ' + symlist)

#Re assigning 3rd element to 'AIG'
symlist[2] = 'AIG'
print(symlist[2])

print('Extracting the first 3 elements' + symlist[0:3])
print('Extracting the last 2 elements' + symlist[-2:])

print('Creating an empty list and appending an item: ')
mysyms = []
mysyms.append('GOOG')
print(mysyms)

