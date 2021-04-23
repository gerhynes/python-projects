import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left. You have used these letters: {' '.join(used_letters)}")

        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("That letter's not in the word")

        elif user_letter in used_letters:
            print("You already used that character. Please try again.")
        
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(f"Oh no. You died. The word was {word}.")
    print(f"Congratulations! You guessed the word was {word}.")

if __name__ == "__main__":
    hangman()