### Week 3 -Assignment 1###
##Write a program that uses a print statement to say 'hello world' as shown in 'Desired Output'.
###Desired output = Hello world

# ***print('Hello World')***

### Week 4- Assignment 2.2###
###Write a program that uses input to prompt a user for their name and then welcomes them.
# Note that input will pop up a dialog box. Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.
###Desired output = Hello Sarah

#***name=input("Enter the name")
#***print('Hello',name)

### Week 4- Assignment 2.3###
###2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
# You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

#*** hours=input('Enter the hours')
# rate=input('Enter the rate per hour')
# hours=float(hours)
# rate=float(rate)
# pay=hours*rate
# print(pay)

### Week 5- Assignment 3.1###
###3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.

# ***hours=input("Enter the hours:")
# rate=input("Enter the rate:")
# hours=float(hours)
# rate=float(rate)
# if hours<=40:
#     pay=hours*rate
#     print(pay)
# if hours > 40:
#     pay = ((hours - 40) * (1.5 * (rate))) + (40 * (rate))
#     print(pay)

### Week 5- Assignment 3.3###
###3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

#*** score=input("Enter score between 0 and 1:")
# score=float(score)
# if score>=1.0 or score<0.0:
#     print("Error")
# elif score >=0.9:
#     print("Grade A")
# elif score >=0.8:
#     print("Grade B")
# elif score>=0.7:
#     print("Grade C")
# elif score>=0.6:
#     print("Grade D")
# elif score <0.6:
#     print("Grade F")

#*****Functions*****
### Week 6- Assignment 4.6###
###4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.

# *** def computepay(hours,rate):
#     if hours<=40:
#         pay=hours*rate
#         #print(pay)
#     else:
#         pay=(hours-40)*(1.5*rate)+(40*rate)
#         #print(pay)
#         return pay
# try:
#     hours=float(input("Enter hours:"))
#     rate=float(input("Enter rate per hour"))
#     print(computepay(hours,rate))
# except:
#     print("Entered a wrong value")


#*****Loops and iteration*****
###Assignment-5.2###
#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered,
# print out the largest and smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
#Desired output -Invalid input
# Maximum is 10
# Minimum is 2
#*** largest=0
# smallest=float('inf')
# while True:
#     number=input("Enter a number")
#     if number=='done':
#         break
#     try:
#         num1 = int(number)
#         if (num1 > largest):
#             largest = num1
#         if num1<smallest:
#             smallest = num1
#     except:
#         print('Invalid input')
#
# print("Maximum is", largest)
# print("Minimum is", smallest)
