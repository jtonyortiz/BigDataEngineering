#None type
email_address = None

#Tuples
s = ('GOOG', 100, 490.1)
#() can be omitted in the syntax:
t = 'GOOG', 100, 490.1

t = () #An empty tuple
w = ('Goog', ) # A 1-item tuple

#Tuple contents are ordered like an array:
v = ('GOOG', 100, 490.1)
name = v[0]
shares = s[1]
price = s[2]

#Displays contents 
print(name)
print(shares)
print(price)


#Tuple Unpacking:
name,shares,price = s #must match the tuple structure:
print('Cost', shares*price)

#Tuples Vs. Lists
#Tuples: Used for a single item consisting of multiple parts
record = ('GOOG', 100, 490.1)
#Lists ususally a collection of distant items, of the same type.
symbols = ['GOOG', 'AAPL', 'IBM']

#Dictionaries:
#Dictionary: Mapping of keys to values
#Also Known as a hashtable or assocative array
sdict = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}

#Common Dictionary operations:
print(s['name'], s['shares'])
print(s['price'])

#Adding and modifying values:
s['shares'] = 75
s['date'] = '6/6/2007'

#Deleteing a value in a dict:
del s['date']


