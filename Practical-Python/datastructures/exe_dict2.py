"""
Author: james Anthony Ortiz
File: exe_dict2.py
Description: Reading from a .csv file into a tuple
"""
import csv
f = open('portfolio.csv')
rows = csv.reader(f)
next(rows)
row = next(rows)


#Create a tuple with the row:
t = (row[0], row[1], row[2])
print('Row represented as a tuple: ',t)
#Declaring new tuple instance
t = (t[0], 75, t[2])
print('New intitial tuple: ', t)

