import random
import os

# Function created to mask the word until guessed
# TO DO: Make sure the user is inputting only letters
# TO DO: Make sure the user is inputting one letter at a time


def asterisker(random_word, guesses):
    result = ""
    for letter in random_word:
        if letter in guesses:
            print(letter, end="")
        else:
            print("*", end="")
    print()
    return result


# word bank from https://github.com/Xethron/Hangman/blob/master/words.txt
def wordselect():
    read_words = open('./hangmanwords.txt').read().splitlines()

    return random.choice(read_words)


random_word = wordselect()

word_len = len(random_word)
letter_list = list(random_word)
guesses = []


print("The word is {} letters long.".format(word_len))
guess_letter = input(" Guess a letter ").lower()
keep_going = True

# Checking if the letter is in the word
while keep_going:
    if guess_letter in random_word:
        print("That letter is correct")
    else:
        print("nope guess again!")
    guesses.append(guess_letter)
    asterisker(random_word, guesses)

# checks if the letter_list set is a subset of guesses then
# keep going becomes false and ends the game.
    if set(sorted(letter_list)).issubset(set(sorted(guesses))):
        keep_going = False
        print("Great job you won!")
    else:
        guess_letter = input(" Guess a letter ")

