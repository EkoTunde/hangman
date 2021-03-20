from random import choice
from typing import ValuesView
from words import words


def start():
    print("Welcome to the hangman! Select your variables, press ENTER to keep default.")
    min = get_config("Min amount of letters (default 5): ", 5)
    max = get_config("Max amount of letters (default 10): ", 10)
    attemps = get_config("How much word guesses? (default 3): ", 3)
    hangman_size = get_config("How big is the hangman? (default 6): ", 6)
    show_hint = get_config("Show hint? Yes [1] or No [0] (defaul = 0): ", 0)

    query = [word for word in words if len(word) >= min and len(word) <= max]
    random_word = choice(query)
    letters = len(random_word)
    board = ("_" * len(random_word))
    taken_letters = []
    errors = 0

    print(
        f"New game started. Max guesses = {attemps} & hangman size = {hangman_size}. A random word was picked from {len(query)} possibilities.\n")

    if show_hint > 0:
        random_letter = choice([char for char in random_word])
        taken_letters.append(random_letter)
        board = update_board(taken_letters, random_word)

    while board != random_word and errors < hangman_size and attemps > 0:
        print("".join([f"{c} " for c in board])+f"  ({letters} letters)")
        print(f"Taken letters " + str(sorted(taken_letters)))
        guess = input("Guess a letter or risk the word: ").lower()
        print()
        msg = ""
        if len(guess) == 1:
            if guess.isalpha():
                if guess in taken_letters:
                    msg += f"{guess} is already taken."
                else:
                    taken_letters.append(guess)
                    if guess in random_word:
                        msg += f"{guess} is correct!"
                        board = update_board(taken_letters, random_word)
                    else:
                        msg += f"{guess} is incorrect. Try again!"
                        errors += 1
            else:
                msg += "Only letters are valid inputs."
        elif len(guess) == letters:
            if guess == random_word:
                board = random_word
                msg += "Indeed"
            elif attemps > 1:
                msg += "Wrong guess!"
                attemps -= 1
            else:
                msg += "Wrong guess! Game over"
        else:
            msg += "That's not a valid input."
        print(
            msg + f". {hangman_size-errors} error(s) left. {attemps} guess(es) left.")
    else:
        if board == random_word:
            print(f"You win!!! :) {board} was the word!")
        else:
            final_guess = input("No errors left. Your guess: ").lower()
            if final_guess == random_word:
                print("Congrats, you win!")
            else:
                print(f"Incorrect, word was \"{random_word}\" :( Game over!")
        restart = input("\nRestart [Y] or Exit [N] ").lower()
        if restart == "y":
            start()
        else:
            print("Goodbye!")


def get_config(msg, default):
    try:
        return int(input(msg))
    except ValueError:
        return default


def update_board(taken_letters, random_word):
    return "".join([c if c in list(taken_letters) else "_" for c in random_word])


start()
