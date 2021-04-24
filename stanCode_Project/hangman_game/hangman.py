"""
File: hangman.py
Name: CHANG I FAN
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This is a hangman game.
    """
    word = random_word().upper()
    word_print = ''
    times = N_TURNS
    guess_record = ''

    # First input.
    for i in range(len(word)):
        word_print += '-'
    print('The word looks like: ' + word_print)
    print('You have ' + str(times) + ' guesses left')
    guess = input('Your guess: ').upper()

    # The following input.
    while True:
        # Check if the user input an alphabet
        if guess.isalpha == False:
            print('illegal format')
            guess = input('Your guess: ').upper()
        # Guess all correct
        elif word == guess:
            print('Your are correct!')
            print('You win!')
            print('The word was: ' + word)
            break
        # The alphabet is more than one
        elif len(guess) > 1:
            print('illegal format')
            guess = input('Your guess: ').upper()
        # The alphabet has guessed
        elif guess in guess_record:
            print('The word looks like: ' + word_print)
            print('You have '+str(times)+' guess left.')
            guess = input('Your guess: ').upper()
        # Guess correct
        elif guess in word:
            word_make = ''
            for i in range(len(word)):
                ch = word[i]
                if ch == guess:
                    word_make += ch
                else:
                    word_make += word_print[i]
            word_print = word_make
            # Check if the word is all correct
            if word_print != word:
                print('The word looks like: ' + word_print)
                print('You have '+str(times)+' guess left.')
                guess_record += guess
                guess = input('Your guess: ').upper()
            else:
                print('Your are correct!')
                print('You win!')
                print('The word was: ' + word)
        # Guess is incorrect
        elif times != 0:
            times -= 1
            # Check if you die.
            if times != 0:
                print('The word looks like: ' + word_print)
                print('You have '+str(times)+' guess left.')
                guess_record += guess
                guess = input('Your guess: ').upper()
            else:
                print('You are completely hung :(')
                print('The word was: ' + word)
                break









def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
