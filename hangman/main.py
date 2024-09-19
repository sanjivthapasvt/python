import string
import random
from words import words

def get_valid_word(words):
    word = random.choice(words).upper() 
    while " " in word or "-" in word:
        word = random.choice(words).upper()
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 6 

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left and have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ",' '.join(word_list))

        user_input = input("Guess a letter: ").upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1 
                print("Letter is not in the word.")
        elif user_input in used_letters:
            print("You have already used this letter. Please try again.")
        else:
            print("Invalid character. Please enter a valid letter.")

    if lives == 0:
        print(f"You lost! The word was {word}.")
    else:
        print(f"Congratulations! You guessed the word {word} correctly.")

hangman()
