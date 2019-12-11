
"""  Python Assignment
    SMIT Certified Python Programming
    Assignment #1
"""

""" Task no.1
    To print a string in a specified manner
"""
print ('Twinkle, twinkle, little star,\n\t  How I wonder what you are !\n\t\t\tUp above the world so high,\n\t\t\tLike a diamond in the sky.')

""" Task no.2
    Write a program to get the python version you are using 
"""
import sys

version = sys.version
print('Your python version is: ', version)

""" Task no.3
    Write a program to display the current date and time
"""
import datetime

CurrentDateAndTime = datetime.datetime.now()

print('The current date and time is: ', CurrentDateAndTime)

""" Task no.4
    Write a program that accepts the radius of a circle from user and prints out its area
"""

r = int(input('Enter radius of the circle: '))
pi = 3.142
area = pi*(r**2)

print('The area of the circle is : ', area)

""" Task no.5
    Write a program to accept the users first and last name and print them in reverse order
"""

Fname = input('Enter your first name : ')
Lname = input('Enter your last name : ')

print(Lname+' '+Fname)

""" Task no.6
    Writ program that takes two input from user and prints their addition
"""

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(num1+num2)
