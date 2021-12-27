#
# Author: James Ortiz
# File: input_and_output.py
# Description: Useing input and output in python.
#

#An example of reciving input: 
user_name = input('Please enter your name: ')
print("Your name in all capitals is ", user_name.upper(), " and has length: ", len(user_name))

#Using type-conversion with input:
user_radius = input('Please enter the radius of the circle ')
radius = float(user_radius)
diameter = 2 * radius
print('The radius is: ', radius, ' and the diameter is: ', diameter)

