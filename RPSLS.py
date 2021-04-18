# Rock-paper-scissors-lizard-Spock template

#Imports
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

# Take the user's name input and turn it into a number.
def name_to_number(name):
    # delete the following pass statement and fill in your code below
    pass

    # convert name to number using if/elif/else

    if name == "rock":
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'Not a valid user name: fail'

# Take the computer's random number from 0 to 4 and turn it into the correct name.
def number_to_name(number):

    # convert number to a name using if/elif/else
    if number == 0:
        return "rock"
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'Number not 0 through 4: fail'


def rpsls(player_choice):
    # print out the message for the player's choice
    print('Player chooses {}'.format(player_choice))

    # convert the player's choice to player_number using the function name_to_number()
    player_num = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_num = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_name = number_to_name(comp_num)
    # print out the message for computer's choice
    print('Computer chooses {}'.format(comp_name))

    # compute difference of comp_number and player_number modulo five
    dif_val = (comp_num - player_num) % 5

    # Determine the winner. Use the rule discussed in lecture that for Item 1 - Item 2, (Item1-Item2)%5 is
    # 1 or 2, then the first Item wins, but if it results in 3 or 4 then the second Item wins. If the value of the
    # calculation is zero (e.g., both players chose the same number) then the result is a tie.
    if dif_val == 0:
        print('Player and computer tie!\n')
        return
    elif dif_val <3:
        print('Computer wins!\n')
        return
    else:
        print('Player wins!\n')

    # test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
# Player choices - hardcoded in. Plays 5 games.
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# End of Rock Paper Scissors Lizard Spock #

