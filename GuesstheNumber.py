# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random


# helper function to start and restart the game
def new_game(s):
    # initialize global variables used in your code here
    print("New Game. Range is from o to {}".format(s))

    print("Number of remaining guesses is {}\n".format(10 if s == 1000 else 7))
    global secret_number
    secret_number = random.randrange(0, s)

    # store this as a global var so that the new games can start with the same range as the previous game
    global last_game_range
    last_game_range = s

    # Set the guess limit depending on the user input range.
    global guess_limit
    guess_limit = 10 if s == 1000 else 7


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    new_game(100)


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    new_game(1000)


def input_guess(guess):
    # main game logic goes here
    global guess_limit
    guess_limit -= 1

    # turn user input from string into integer
    guess = int(guess)
    print("Guess was {}".format(guess))
    print("Number of remaining guesses is {}".format(guess_limit))

    # if the user is out of guesses, start a new game that has the same range as last game
    if guess_limit == 0:
        new_game(last_game_range)

    # if user gets number correct, print Correct and start new game with range same as last game
    elif secret_number == guess:
        print("Correct!")
        new_game(last_game_range)

    # If user still has guesses but hasn't guessed the number yet, give hints
    elif secret_number > guess:
        print("Higher")
    else:
        print("Lower")


# create frame
frame = simplegui.create_frame("Guess the Number Game", 200, 200)
frame.set_canvas_background('Pink')
button_low_range = frame.add_button("[0,100)", range100)
button_big_range = frame.add_button("[0,1000)", range1000)
user_input = frame.add_input("Enter a guess:", input_guess, 200)

# call new_game, initial game starts with range 0 to 100 not inclusive
new_game(100)

frame.start()
# always remember to check your completed program against the grading rubric
