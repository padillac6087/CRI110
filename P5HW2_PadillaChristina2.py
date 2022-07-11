# A simple Math Quiz with menu
# 07/09/2022
# CTI-110 P5HW2 - Math Quiz
# Christina V Padilla
#

#Import random
import random

#Random number function
def Create_Random_Number():
 randomNumber = random.randint(1, 1000)
 return randomNumber

#Function to ask user for answer
def Ask_User_Number(message="Enter answer.\n"):
 answer = float(input(message))
 return answer

def Ask_Again(message="\ntry again: "):
 answer = float(input(message))
 return answer
 
#def main menu for game
def main():
 userCongratulated = False
 start = True
 counter = 0
 print("""
   Main Menu
   ---------------
   1. Add Random Number
   2. Subtract Random Number
   3. Exit
   """)
 choice = int(input("Please choose one of the menu options: "))
#addition
 if choice == 1:
     
   a = Create_Random_Number()
   b = Create_Random_Number()
   right = a + b
   print("  ",a, " \n+ ", b)
   while userCongratulated == False:
     counter = counter + 1
     if start == True:
       answer = Ask_User_Number()
       start = False
     else:
       answer = Ask_Again()
     
     if answer == right:
       print("Congratulations!!!! your answer is correct..")
       print("Number of guesses: ", counter)
       main()
     elif answer < right:
       print("Sorry, guess is too low.")
     else:
       answer > right
       print("Sorry, guess is too high.")
       
 if choice == 2:
#subtration
   a = Create_Random_Number()
   b = Create_Random_Number()
   right = a - b
   print("  ", a, " \n- ", b,)
   while userCongratulated == False: #Call menu regardless of answer
     counter = counter + 1
     if start == True:
       answer = Ask_User_Number()
       start = False
     else:
       answer = Ask_Again()
       
     if answer == right:
       print("Congratulations!!!! your answer is correct..")
       print("Number of guesses: ", counter)
       main()
     elif answer < right:
       print("Sorry, guess is too low.")
     else:
       answer > right
       print("Sorry, guess is too high.")
   
 if choice == 3:
   print('Thank you for playing...')
   print("Bye!!")
   exit()

 if choice >= 4:
    print("Invalid menu option.")
    main()

if __name__ == '__main__':
 main()

