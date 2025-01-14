import random
from guess import suggest_next_letter, play_move
from your_solution import suggest_next_letter_sol

"""
This file is the Hangman game. 
Please do not edit this file in any case or you might not be able to test you code.
You need to implement your logic in guess.py in suggest_next_letter function.
However you should go through this code too for better understanding of the mechanics of the game.
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--sample", type=bool)
parser.add_argument("--play", type=bool)


def choose_word(filename):
    """choosing random word samples
    """
    with open(filename, 'r') as file:
        words = file.readlines()
    return random.choice(words).strip()


def display_word(word, guessed_letters):
    """
    word display for terminal

    """
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word


def hangman(filename, guess_func):
    """
    actual logic of the game.
    """
    # word = choose_word(filename)
    file_path = "training.txt" 
    with open(file_path, "r") as file:
        data = file.read().splitlines()

    processed_words = []
    for word in data:
        if word.isalpha():
            processed_words.append(word.lower())

    words = processed_words
    count = 0
    # print(len(words))
    # return
    for i, word in enumerate(words[-1000:]):
        print(f"iteration : {i}" )
        # print("hiii")
        print(word)
        # print('hello')
        guessed_letters = []
        attempts_left = 6

        # print("Welcome to Hangman!")
        # print("Try to guess the word by guessing a letter at a time. You have 6 attempts.")
        # print(display_word(word, guessed_letters))

        while attempts_left > 0:
            guess = guess_func(display_word(word, guessed_letters), guessed_letters)
            # print(f"You guessed the letter: {guess}")
            if guess in guessed_letters:
                # print("You've already guessed that letter.")
                attempts_left -= 1
                # print("Attempts left:", attempts_left)
                print(' '*45)
                continue

            guessed_letters.append(guess)
            
            if guess not in word:
                # print("Correct!")
                
            # else:
                # print("Incorrect!")
                attempts_left -= 1

            # print(display_word(word, guessed_letters))
            # print(count)
            if '_' not in display_word(word, guessed_letters):
                # print("Congratulations! You've guessed the word.")
                count += 1
                print(f"correct guess, count : {count}")
                break

            # print("Attempts left:", attempts_left)
            # print(' '*45)

        # print("Out of attempts! The word was:", word)
    print(f"% Accuracy : {count * 100 / float(len(words[-1000:]))}")


if __name__ == "__main__":
    # args = parser.parse_args()
    
    # if args.play:
    #     hangman("training.txt", play_move)
    # elif args.sample:
    #     hangman("training.txt", suggest_next_letter)  
    # else:
        hangman("training.txt", suggest_next_letter_sol)