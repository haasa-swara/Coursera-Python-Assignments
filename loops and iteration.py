#*****Loops and iteration*****
###Assignment-5.2###
#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, 
#print out the largest and smallest of the numbers. If the user enters anything other than a valid numbercatch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
#Desired output -Invalid input
# Maximum is 10
# Minimum is 2
largest=0
smallest=float('inf') ## Taking smallest as infinity
while True:
    number=input("Enter a number")
    if number=='done':
        break
    try:
        num1 = int(number)
        if (num1 > largest):
            largest = num1
        if num1<smallest:
            smallest = num1
    except:
        print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)
