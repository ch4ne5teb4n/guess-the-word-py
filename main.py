from easygui import *
import random

WORDS = ["zephyr", "sobriquet", "rhythm", "bourgeoisie", "iridescence"]

def choose_word():
    return random.choice(WORDS)

def display_word(word, guessed_letters):
    return "".join(letter if letter in guessed_letters else "_" for letter in word)

def get_guess():
    return enterbox("Guess a letter or the whole word:")

def process_single_letter_guess(letter, word, guessed_letters):
    if letter in word:
        if letter not in guessed_letters:
            guessed_letters.append(letter)
            return f"Awesome possum! The letter '{letter}' is in the word!"
        else:
            return f"You already guessed the letter '{letter}'. Try with another letter."
    else:
        return f"Sorry, the letter '{letter}' is not in the word."

def main():
    word_to_be_guessed = choose_word()
    guessed_letters = []
    guess_count = 0

    while True:
        displayed_word = display_word(word_to_be_guessed, guessed_letters)
        guess = enterbox(f"Guess the word: {displayed_word}\n\nGuess a letter or the whole word:")

        if guess is None:
            msgbox("Game over. Better luck next time!")
            break

        guess = guess.lower()
        guess_count += 1

        if guess == word_to_be_guessed:
            msgbox(f"Congratulations! You guessed the word '{word_to_be_guessed}' in {guess_count} guesses.")
            break
        elif len(guess) == 1:
            feedback = process_single_letter_guess(guess, word_to_be_guessed, guessed_letters)
            msgbox(feedback)
        else:
            msgbox("Sorry, that's incorrect. Try again!")

        if all(letter in guessed_letters for letter in word_to_be_guessed):
            msgbox(f"Great job! You've guessed the '{word_to_be_guessed}' in {guess_count} guesses!")
            break

main()