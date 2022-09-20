# Number Guessing Game
#  import random

winning_number = 76
num = int(input("Enter a number: "))
while(num != winning_number):
    if num > winning_number:
        print("Number is too high")
    elif num < winning_number:
        print("Number is too low")
    else:
        print("You Win!!!")
    num = int(input("Enter a number: "))