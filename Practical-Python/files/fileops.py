"""
Author: James Anthony Ortiz
File: fileops.py
Description: File-operations in Python
"""
import os
f = open('versos.txt', 'rt')
        
#Read file line-by-line:
with f as file:
    data = file.read()
print(data)


#Obtain location of file
print(os.getcwd())