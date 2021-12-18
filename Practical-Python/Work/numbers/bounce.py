"""
Author: James Anthony Ortiz
File: bounce.py
Description: A rubber ball is dropped from a height of
100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. 
Write a program bounce.py that prints a table showing the height of the first 10 bounces.
"""

ball = 100
counter = 1
while(counter < 11):
    ball = ball * 3/5
    print(counter, round(ball, 4))
    counter = counter + 1
