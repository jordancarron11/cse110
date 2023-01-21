import random
play = "yes"
rotationCount = 1
#decides if the user keeps playing again and only iterates if the user chooses yes
while play == "yes":
    randomNumber = random.randint(1,100)
    userGuess = int(input("What is your guess from 1-100? "))
    #is the counter while loops and helps the user decide to choose higher or lower and lets them know when they finished
    while randomNumber != userGuess:
        #counts how many times the while loop has iterated so we can track how many guesses the user took. 
        rotationCount += 1    
        if randomNumber > userGuess:
            print("Sorry, guess higher\n")
            userGuess = int(input("What is your guess from 1-100? "))
        elif randomNumber < userGuess:
            print("Sorry guess lower\n")
            userGuess = int(input("What is your guess from 1-100? "))
        else:
            print("Sorry that is not a correct input")
            userGuess = int(input("What is your guess from 1-100? "))
    #when the player guesses the right screen this executes to tell them how they did and asks if they want to go again
    print(f"\ncongrats {userGuess} is correct! You guessed {rotationCount} times before getting the right answer")
    playAgain = input("Want to play again? ")
    if playAgain == "yes":
        play = "yes"
    else:
        play = "no"