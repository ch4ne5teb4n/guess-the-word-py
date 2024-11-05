from easygui import *
import random

words = ["zephyr", "sobriquet", "rhythm", "bourgeoisie", "iridescence"]
word_to_be_guessed = random.choice(words)
guessed_letters = []
guess_count = 0

while True:
    displayed_word = ""
    for letter in word_to_be_guessed:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
            
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
        if guess in word_to_be_guessed:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                msgbox(f"Awesome possum! The letter '{guess}' is in the word!")
            else:
                msgbox(f"You already guessed the letter '{guess}'. Try with another letter.")
        else:
            msgbox(f"Sorry, the letter '{guess}' is not in the word.")
    else:
        msgbox("Sorry, that's incorrect. Try again!")

    if all(letter in guessed_letters for letter in word_to_be_guessed):
        msgbox(f"Great job! You've guessed the '{word_to_be_guessed}' in {guess_count} guesses!")
        break