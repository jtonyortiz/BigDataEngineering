#
# Author: James Ortiz
# File: control_structures.py
# Description: Control Structures in Python
#
#

#Basic while-loop in python:
counter = 1
while counter <= 5:
    print('Hello, world')
    counter = counter + 1

#For loop in Python:
for item in [1, 3, 6, 2, 5]:
    print(item)

print('For loop with a range statement')

#For loop with a range statement:
for item in range(5):
    print(item ** 2)
    
#Iterating through each letter in a list of strings:
word_list = ['Cat', 'dog', 'rabbit']
letter_list = []
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)


sq_list = []
for x in range(1, 11):
    sq_list.append(x * x)
    
print('List of squares from 1 to 10: ', sq_list)

#List comprehension 
sq_list = [(x * x) for x in range(1, 11)]
print('List useing list-comprehension: ', sq_list)

sq_list = [x *x for x in range(1, 11) if x % 2 != 0]
print('Odd numbers in the squared list: ', sq_list)

cons_list = [ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
print('Display consonsants in comprehension: ', cons_list)







