#
# Author: James Ortiz
# File: dictionaries.py
# Description: Dictionaries in python
#
#

#Example of a Dictionary:
capitals = {'Iowa': 'Des Moines', 'Wisconsin': 'Madison'}
print('Print Dictionary: ', capitals)

#Adding a Key-Value pair:
capitals['Utah'] = 'Salt Lake City'
print('Added k-v to dictionary: ', capitals)
capitals['California'] = 'Sacramento'
print('Printing all fo the key-value pairs:')
for k in capitals:
    print(capitals[k], "is the capitol of ", k)
    

#Adding an Extension to the Phone:
phone_ext = {'david': 1410, 'Brad': 1137}
print('Printing phone extension: ', phone_ext)
print('Printing keys from the phone extnension: ', phone_ext.keys())
print('Creating a list from the keys in the phone ext: ', list(phone_ext.keys()))

