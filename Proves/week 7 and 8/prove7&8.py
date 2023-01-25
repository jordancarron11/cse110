import random
import dictionary
play_again ='yes'
while play_again == 'yes':
    

   

    print('Welcome to the word guessing game!\n')
    difficulty = input("Which difficulty do you want? easy(e), normal(n), hard(h) type (e/n/h): ").lower()
    if difficulty == 'e':
        secret_word = random.choice(dictionary.Five)
    elif difficulty == 'n':
        secret_word = random.choice(dictionary.Six)
    elif difficulty == 'h':
        secret_word = random.choice(dictionary.Seven)
    else: 
        print("Sorry that is not a valid imput please enter either e for easy n for normal or h for hard")
        difficulty = input("Which difficulty do you want? easy(e), normal(n), hard(h) type (e/n/h): ").lower()
    hint = ' _ ' * len(secret_word)    
    print(f'Your hint is: {hint}')

    guess = input('What is your guess? ')
    guess_count = 0
    guessed_correctly = False
    def process_guess(secret_word, guess):
        position = 0
        hint = ''
        for letter in guess:
            if letter == secret_word[position]:
                hint += f' {letter.upper()}'
            elif letter in secret_word:
                hint += f' {letter.lower()}'
            else:
                hint += ' _ '
            position += 1
        print(f'Your hint is: {hint}')
        return hint

    while guess.lower() != secret_word:

        if len(guess) != len(secret_word):
            print('\nWelcome to the word guessing game!\n')
            print(f'Sorry, the guess must have {len(secret_word)} letters')
            print('Press enter to continue.')
            input()
            print(f'\nYour hint is: {hint}')
            guess = input('What is your guess? ')
            guess_count += 1
        else:
            print('\nWelcome to the word guessing game!\n')
            guessed_correctly = process_guess(secret_word, guess)
            guess = input('What is your guess? ')
            guess_count += 1
   
    print('\nCongratulations! You guessed it!')
    print(f'It took you {guess_count} guesses.\n')
    play_again = input("would you like to play again?(yes/no)")
