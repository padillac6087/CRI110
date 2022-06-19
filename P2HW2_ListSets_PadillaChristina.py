#This program will take numbers and create both a list and set
#CTI-110
#P2HW2-List and Sets
#Your Name
#Date
#
#Ask the user to enter 6 numbers
num1 = float(input('Enter num 1: '))
num2 = float(input('Enter num 2: '))
num3 = float(input('Enter num 3: '))
num4 = float(input('Enter num 4: '))
num5 = float(input('Enter num 5: '))
num6 = float(input('Enter num 6: '))
#Take the user entered numbers and add it to a list
list1 = [num1,num2,num3,num4,num5,num6]
#Take the list and turn it into a set
set1 = set(list1)
print()
#Show the user the list they created
print('Created list\n',list1)
#Show the user the smallest number
print('Smallest number in list:',min(list1))
#Show the user the largest number
print('Largest number in list:',max(list1))
#Show the user the sum of all the numbers together
print('Sum of numbers in List:',sum(list1))
#Show the user the average number by getting the sum and dividing it by 6
print('Average of numbers in List:',sum(list1)/6)
print()
#Show the user their list as a set
print('Created set\n',set1)
