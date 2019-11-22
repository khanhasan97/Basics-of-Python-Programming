
"""  Python Assignment
    SMIT Certified Python Programming
    Assignment #3
"""

""" Task no.1
    Make a calculator using Python with addition , subtraction , multiplication ,
    division and power.
"""
num1 = int(input('Enter first number: '))
operator = input('Enter operator: ')
num2 = int(input('Enter second number: '))

if operator == '+':
    num = num1 + num2
    print('The sum of th two numbers is: ', num)
elif operator == '-':
    num = num1 - num2
    print('The difference of the two numbers is: ', num)
elif operator == '*':
    num = num1 * num2
    print('The product of the two numbers is: ', num)
elif operator == '^':
    num = num1 ** num2
    print('{} to the power {} is: '.format(num1, num2), num)
else:
    print('Enter correct operator !!')

""" Task no.2
    Write a program to check if there is any numeric value in list using for loop
"""
list1 = ['Hasan', 45, 'Ali', 34.456, 61, 38.2, 'Khan', 40]
list2 = []
for i in range(0, len(list1)):
    if type(list1[i]) == int:
        list2.append(list1[i])
print('\nThe numeric values is list 1 are: ', list2)

""" Task no.3
   Write a Python script to add a key to a dictionary
"""

Python_Dictionary = {'Course': 'Python Programming '}
Python_Dictionary['Mode'] = 'Online'

print('\n', Python_Dictionary)

""" Task no.4
    Write a Python program to sum all the numeric items in a dictionary
"""
Sample = {'apples': 4, 'Course': 'Python', 'oranges': 9, 'Name': 'Hasan', 'Mangoes': 8, 'kiwis': 5}
sum_of_nums = 0
for value_of_key in Sample.values():
    if type(value_of_key) == int:
        sum_of_nums += value_of_key
print('\nThe sum of all numeric items in dictionary is: ', sum_of_nums)

""" Task no.5
    Write a program to identify duplicate values from list
"""
list3 = [1, 4, 6, 'one', 1, 'one', 4, 'two', 7, 5, 6]
Duplicate = []

for i in range(0, len(list3)):
    for j in range(0, len(list3)):
        if list3[i] == list3[j] and i != j:
            Duplicate.append(list3[i])
print('\n', Duplicate, '\n')

""" Task no.6
    Write a Python script to check if a given key already exists in a dictionary
"""
Sample_Dict = {'Name': 'Hasan', 'Roll no.': 'TC-61', 'Department': 'Telecom', }
k = input('Enter key: ')
count = 0
for key_of_Dict in Sample_Dict.keys():
    if key_of_Dict == k:
        count = 1
if count == 1:
    print('\nKey already exists !')
else:
    v = input('Enter value: ')
    Sample_Dict[k] = v

print('\n', Sample_Dict)


