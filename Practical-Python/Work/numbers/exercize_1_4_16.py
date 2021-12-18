"""
Author: James Anthony Ortiz
File: exercize_1_4_16.py
Description: 
"""

symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
print(symbols.lower())

symbols2 = 'AAPL,IBM,MSFT,YHOO,SCO'
#Find values in Strings:
print(symbols2.find('MSFT'))

#Print values in between indexes [13:17]
print(symbols2[13:17])

#Replace values 
symbols2 = symbols2.replace('SCO', 'DOA')
print(symbols2)


name = '   IBM   \n'
name = name.strip()
print(name)
