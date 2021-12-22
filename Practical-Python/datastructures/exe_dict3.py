import csv
f = open('portfolio.csv')
rows = csv.reader(f)
next(rows)
row = next(rows)

#Useing a dictionary as a data-structure
d = {
    'name': row[0],
    'shares': int(row[1]),
    'price': float(row[2])
}

#Displaying the dictionary:
print('Displaying a dictionary: ', d)

print('Display the total cost of holding: ', d['shares'] * d['price'])

#Modifying dshares:
d['shares'] = 75
print('Display new dict with shares val modified: ', d)

#Dictionaries can be feely modified: 
d['date'] = (6, 11, 2007)
d['account'] = 12345
print('Newly modified dictionary: ', d)

#Printing all of the keys with list()
print('Obtaining the keys with list: ', list(d))


#Useing a loop to iterate through the dictionary 
#Used to read dictionary content in key value order:
print('iterating with a for-loop useing a dictionary:')
for k in d:
    print(k, '=', d[k])



#Displaying Key, Value tuples with the items() method:
items = d.items()
for k, v in d.items():
    print(k, '=', v)


