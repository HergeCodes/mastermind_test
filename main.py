import random

#generate random number
def game_start(mode):
    list = []
    if mode == 1:
        print("WELCOME TO MASTERMIND - EASY MODE")
        for i in range(0, 4):
            n = random.randint(0, 9)
            list.append(n)

        return list, mode
    elif mode == 2:
        print("WELCOME TO MASTERMIND - NORMAL MODE")
        for i in range(0, 4):
            n = random.randint(0, 9)
            list.append(n)

        return list, mode
    elif mode == 3:
        print("WELCOME TO MASTERMIND - HARD MODE")
        for i in range(0, 5):
            n = random.randint(0, 9)
            list.append(n)

        return list, mode

#compare guess and random number
def compare_guess(number, guess, gamemode):
    listguess = [int(x) for x in str(guess)]
    listNumbersCorrect = []
    numbersCorrect = 0
    #easy mode
    if gamemode == 1:
        for i in range (0, len(number)):
            if number[i] == listguess[i]:
                numbersCorrect += 1
                listNumbersCorrect.append(listguess[i])

        return numbersCorrect, listNumbersCorrect
    #normal / hard mode
    elif gamemode == 2 or gamemode == 3:
        for i in range(0, len(number)):
            if number[i] == listguess[i]:
                numbersCorrect += 1

        return numbersCorrect, listNumbersCorrect

#game menu
print("Easy - 1\nNormal - 2\nHard - 3")
while True:
    try:
        gamemode = int(input("Enter the gamemode : "))
        if gamemode > 3 or gamemode < 1:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid integer.")

#get random number and gamemode
gamestart = game_start(gamemode)
pcnumber = gamestart[0]
gamemode = gamestart[1]

#cheat mode
print(pcnumber)

#assign variable
numbersCorrect = 0
tries = 1

#easy mode
if gamemode == 1:
    while numbersCorrect != 4:
        while True:
            try:
                guess = input("Enter a four-digit guess : ")
                if len(str(guess)) != 4:
                    #print("len error")
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid integer")
        compareGuessResults = compare_guess(pcnumber, guess, gamemode)
        numbersCorrect = compareGuessResults[0]
        listNumbersCorrect = compareGuessResults[1]
        if numbersCorrect == 4:
            print("Congratulations, your number was correct, you guessed it in", tries, "tries")
        else :
            print("You got", numbersCorrect,"numbers correct and they were \n" + str(listNumbersCorrect)[1:-1])
            tries += 1
#normal mode
elif gamemode == 2:
    while numbersCorrect != 4:
        while True:
            try:
                guess = input("Enter a four-digit guess : ")
                if len(str(guess)) != 4:
                    #print("len error")
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid integer")
        compareGuessResults = compare_guess(pcnumber, guess, gamemode)
        numbersCorrect = compareGuessResults[0]
        if numbersCorrect == 4:
            print("Congratulations, your number was correct, you guessed it in", tries, "tries")
        else:
            print("You got", numbersCorrect, "numbers correct, try again.")
            tries += 1
#hard mode
elif gamemode == 3:
    while numbersCorrect != 5:
        while True:
            try:
                guess = input("Enter a five-digit guess : ")
                if len(str(guess)) != 5:
                    #print("len error")
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid integer")
        compareGuessResults = compare_guess(pcnumber, guess, gamemode)
        numbersCorrect = compareGuessResults[0]
        if numbersCorrect == 5:
            print("Congratulations, your number was correct, you guessed it in", tries, "tries")
        else:
            print("You got", numbersCorrect, "numbers correct, try again.")
            tries += 1
