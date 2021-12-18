
"""
Author : James Anthony Ortiz
File: string_ext_1_4.py
Description: String extration with python
"""

symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
print(symbols[0]) #pirnts 'A'
print(symbols[1]) #prints 'A'
print(symbols[2]) #prints 'P'
print(symbols[-1]) #prints 'O'
print(symbols[-2]) #prints 'C'

# Concatenate GOOG to the End of the string:
symbols = symbols + ',GOOG'
print(symbols)

#Append to the front of the symbosl string 'HPQ'
symbols = 'HPQ,' + symbols
print(symbols)

#Membership checking:
print('Checking for Membership: ')
if 'IBM' in symbols:
    print('True')
if 'AA' in symbols:
    print('True')
if 'CAT' in symbols:
    print('True')

