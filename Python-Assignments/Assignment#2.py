"""  Python Assignment
    SMIT Certified Python Programming
    Assignment #2
"""

""" Task no.1
    Write a program which takes 5 inputs from user for different subject’s
    marks, total it and generate mark sheet using grades 
"""
sub1 = int(input("Enter marks of maths: "))
sub2 = int(input("Enter marks of physics: "))
sub3 = int(input("Enter marks of chemistry: "))
sub4 = int(input("Enter marks of english: "))
sub5 = int(input("Enter marks of urdu: "))

if (sub1 or sub2 or sub3 or sub4 or sub5) > 100:
    print("Error in entering marks !")
else:
    total_Marks = sub1 + sub2 + sub3 + sub4 + sub5
    Grade = (total_Marks/500)*100

    # applying grading conditions through if else statements
    if 80 <= Grade < 100:
        print("\nYou have achieved A grade !")
    elif 70 <= Grade < 80:
        print("\nYou have achieved B grade !")
    elif 60 <= Grade < 70:
        print("\nYou have achieved C grade !")
    else:
        print("\nYou have failed the semester !")

""" Task no.2
    Write a program which take input from user and identify that the given
    number is even or odd 
"""

num = int(input("\nEnter a number: "))
if num % 2 == 0:
    print("It is an even number! ")
elif num % 2 == 1:
    print("It is an odd number!")

""" Task no.3
   Write a program which print the length of the list
"""
list1 = ['maths', 'english', 'physics', 'chemistry', 'biology']

print("\nThe length of the list 1 is: ", len(list1))

""" Task no.4
   Write a Python program to sum all the numeric items in a list
"""

list2 = ['basketball', '6', 'football', '899', 'Cricket', '45', '19']
total = 0
for i in range(0, len(list2)):
    if list2[i].isdigit():
        total += int(list2[i])

print("\nThe sum of all numbers in list 2 is: ", total)

""" Task no.5
   Write a Python program to get the largest number from a numeric list
"""

list3 = [45, 54, 23, 51, 47, 60]
max_num = list3[0]
for i in range(1, len(list3)):
    if list3[i] > list3[i-1]:
        max_num = list3[i]
print("\nThe largest number is: ", max_num, '\n')

""" Task no.6
    write a program that prints out all the elements of the list that are
    less than 5
"""

list4 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in range(0, len(list4)):
    if list4[i] < 5:
        print(list4[i], end=' ')


