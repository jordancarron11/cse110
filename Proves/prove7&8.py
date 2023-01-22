import random

play = "yes"
start = '------'
correctWord = "jordan"
userWordChoice = input("What is your five letter word? ")


def correctLetterRightPlace():
    if start[0] == userWordChoice [0]:
        start[0] = userWordChoice[0].upper()
    elif start[1] == userWordChoice[1]:
        start[1] = userWordChoice[1].upper()
    elif start[2] == userWordChoice [2]:
        start[2] = userWordChoice [2].upper()
    if start[3] == userWordChoice [3]:
        start[3] = userWordChoice[3].upper()
    elif start[4] == userWordChoice[4]:
        start[4] = userWordChoice[4].upper()
    return start

def correctLetterwrongPlace9():
    if correctWord[0] == userWordChoice [1,2,3,4]:
        start[1,2,3,4] = userWordChoice[0].lower()
    elif correctWord[1] == userWordChoice[0,2,3,4]:
        start[0,2,3,4] = userWordChoice[1].lower()
    elif correctWord[2] == userWordChoice [0,1,3,4]:
        start[0,1,3,4] = userWordChoice [2].lower()
    if correctWord[3] == userWordChoice [0,1,2,4]:
        start[0,1,2,4] = userWordChoice[3].lower()
    elif start[4] == userWordChoice[0,1,2,3]:
        correctWord[0,1,2,3] = userWordChoice[4].lower()    
    return start

while userWordChoice != correctWord:
    if userWordChoice[0,1,2,3,4] == correctWord [0,1,2,3,4]:
        correctLetterRightPlace()

    

    
    
    
print(f"Congratualtions! you guessed the word which was {correctWord}")
playAgain = input("Want to play again (yes/no)? ")
if playAgain == 'yes':
        play == 'yes'
else:
        play == 'no'
        
    