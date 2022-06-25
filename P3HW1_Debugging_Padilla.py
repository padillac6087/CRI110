#Debugging Grades
#06/14/2022
#CTI-110 P3H1 - Debugging
#Christina V Padilla

#This program takes a number grade and outputs a letter grade.
def main():
#system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
#ask user their score
    score = float(input('Enter grade: '))
#use if-esle statments to decide the letter grade
    if score >= 90:
        print('Your grade is: A')

    elif score >= 80:
        print('Your grade is: B')

    elif score >= 70:
        print('Your grade is: C')

    elif score >= 60:
        print('Your grade is: D')
    
    else:
        print('Your grade is: F')
    
main()
