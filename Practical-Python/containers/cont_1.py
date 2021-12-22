"""
Author: James Ortiz
File: cont_1.py
Description: Tutorial on Lists, Dictionaries, and Sets
"""

#Lists as a Container:
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
]

print(portfolio[0]) #Displays ('GOOG', 100, 490.1)

#Sets:
#Sets are a collection of unordered unique items:
tech_stocks = {'IBM', 'AAPL', 'MSFT'}
#Alternative Syntax:
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])

#List consturction:
records = []
#Use .append() to add more items:
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
print('List of the records as tuples: ', records)

#Dictioonaries as a Container:
prices = {
    'GOOG': 513.25,
    'CAT': 87.22,
    'IBM': 93.37,
    'MSFT': 44.12
}

print('Prices for IBM: ',prices['IBM'])
print('Prices for Google: ', prices['GOOG'])

#Dictionary Consturuction:
print(prices.get('IBM', 0.0))

#Composite Keys:
holidays = {
    (1, 1): 'New Years',
    (3, 14): 'Pi Day',
    (9,13): 'Programmer'/'s day',
}

print('Printing out to value for Pi Day: ', holidays[3, 14])

#Sets in Python:
#Sets arw a collection of unordered unique items:
tech_stocks = {'IBM', 'AAPL', 'MSFT'}
#Alternative syntax:
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])

print('Tech - Stocks as a set: ', tech_stocks)

#Additional Set Operations:
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']
print('Names of a list: ', names)
unique = set(names)
print('names after the list becomes a set: ', unique)

#Additonal Set Operations:
unique.add('CAT') #Adding an item
unique.remove('YHOO') #Removing an item:

s1 = {'a', 'b', 'c'}
s2 = {'c', 'd'}

print('Union operation on set: with |', s1 | s2)
print('Intersection operation on set: ', s1 & s2)
print('Differnce of two sets: ', s1-s2)

