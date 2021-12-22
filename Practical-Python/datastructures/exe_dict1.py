"""
Author: James Anthony Ortiz
File: exe_dict1.csv
Description: Opening csv to process into dictionary
"""
import csv
f = open('portfolio.csv')
rows = csv.reader(f)
next(rows)
print('First row: ', next(rows))
row = next(rows)
print('Next-Row: ',row)
