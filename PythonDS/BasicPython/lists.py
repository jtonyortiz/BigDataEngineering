#
# Author: James Ortiz
# File: lists.py
# Description: Lists in Python with methods
#

#Lists and their methods:
print('First example: ')
my_list = [1, 2, 3, 4]
A = my_list * 3
print(A)
my_list[2] = 45
print(A)

print('Second Example: ')
my_list = [1024, 3, True, 6.5]
my_list.append(False)
print(my_list)
my_list.insert(2,4.5)
print(my_list)
print(my_list.pop())
print(my_list)
print(my_list.pop(1))
print(my_list)
my_list.pop(2)
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.count(6.5))
print(my_list.index(4.5))
my_list.remove(6.5)
print(my_list)
del my_list[0]
print(my_list)