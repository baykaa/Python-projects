# Exercise - 1
# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. 
#Write a function which is given the day number, and it returns the day name (a string).

# weeks_name = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
# def week(number):
#     return weeks_name[number]
# print(week(0))

# Exercise - 2
# weeks_name = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
# start_day = int(input("Start day: "))
# len_stay = int(input("Length of stay: "))
# day_return = (start_day + len_stay) % 7
# print("You will return on: ", weeks_name[day_return])

#Exercise 3

# a > b | a <= b
# a >= b | a < b
# a >= 18  and  day == 3 | a <18 or day != 3
# a >= 18  and  day != 3 | a >18 or day == 3

# Exercise - 10

# def find_hypot(a, b):
#     return (a **2 + b **2) ** 0.5

# import math

# def is_rightangled(a,b,c):
#     # if square root of (a^2 + b^2) is equal to c then it is right angled
#     root = (a**2 + b**2) ** 0.5
#     print("Root: ", root)
#     print("c: ", c)
#     print(abs(c-root))
#     if abs(c-root) < 0.000000001:
#         return True
#     else: 
#         return False

# print(is_rightangled(10,24,26))

# import time
# i = 10
# while i >= 1:
#     print(i)
#     time.sleep(1) # sleep for 1 second
#     i -= 1

# print('Hapy new year!') 

# import random # We cover random numbers in the
# rng = random.Random() # modules chapter, so peek ahead if you want. "rn!
# number = rng.randrange(1, 1000) # Get random number between {1 and 1000).
# guesses = 0
# message = ""
# while True:
#     guess = int(input(message + "\nGuess my number between 1 and 1000: "))
#     guesses += 1
#     if guess > number:
#         message += str(guess) + " is too high.\n"
#     elif guess < number:
#         message += str(guess) + " is too low.\n"
#     else:
#         break
# input("\n\nGreat, you got it in "+str(guesses)+" guesses!\n\n") 

#Exercise 1. Write a program to count the number of digits in a positive integer
count = 0
number = int(input("Number: "))
if number > 0:
    number = str(number)
    for i in number:
        count += 1
        print(count)
    print(f"Total digit of inputted number: {count}")  
else:
    print("Please input positive number!")
    
# Exercise 2. Write a program to count the number of digits 0 or 5 in a positive ingeger. 

# count = 0
# number = int(input("Number: "))
# if number > 0:
#     number = str(number)
#     for i in number:
#         if i == '0' or i == '5':
#             count += 1
#     print(f"Total count of 0 and 5: {count}")  
# else:
#     print("Please input positive number!")

# input = int(input("Number: "))
# while input > 5:
#     print(input ,"is geater than 5")
#     input -= 1

    