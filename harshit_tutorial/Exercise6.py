num = int(input("Guess a number between 0 and 100: "))
win = 43
i = 1
while True:
    if num > win:
        print("too high")
    elif num < win:
        print("too low")
    else:
        print("You win , and you guessed this number in",i,"times")
        break
    num = int(input("Guess again: "))
    i +=1
