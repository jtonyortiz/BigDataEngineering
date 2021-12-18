"""
Author: James Anthony Ortiz
File: lists_1_5.py
Description: Introduction to Lists in Python
"""
#Lists are created as such:
names = ['Elwood', 'Jake', 'Curtis']
nums = [39, 38, 42, 65, 111]

#Splitting a string to create a list:
line = 'GOOG,100,400,490.10'
row = line.split(',')
print(row)

#List Operations
#Lists can hold items of any type. Add New Items with append()
names.append('Murphy')
names.insert(2, 'Aretha')

#Use + to concatenate lists:
s = [1, 2, 3]
t = ['a', 'b']
print(s + t)

#Lists are indexed by integers
print('lists are indexed by integers beginnign with 0')
names = ['Elwood', 'Jake', 'Curtis']
print(names)
print(names[0])
print(names[1])
print(names[2])

#Negative Indices count from the end.
print('Negative indices count from the end')
print(names[-1])

#Modify any item in the list:
print('Modify any item in the list: ..Adding Joliet Jake')
names[1] = 'Joliet Jake'
print(names)

#Print the length of a list:
print('Print the length of a list:')
print(len(names))

#Performing a membership test:
print('Membership test:')
if 'Elwood' in names:
    print('This prtins true if Elwood is in the names list')

if 'Britney' not in names:
    print('This prints true - if Britney is not in names')

#Replication on a list:
print('Replication s*n')
print(s*3)

#Iterating over a list:
print('Iterating over a list:')
for name in names:
    print(name)

#Finding the index of an element in a lsit:
print('Finding curtis in names list:' + names.index('Curtis'))


#List removal:
print('List removal can be preformed by useing .remove(), or keyword del')
del names[1]

#List Sorting
print('Lists can be sorted in-place:')
s = [10, 1, 7, 3]
print(s)
s.sort()
print(s)

#Sorting in reverse order:
print('Sorting in reverse order:')
s = [10, 1, 7, 3]
s.sort(reverse=True)
print(s)



