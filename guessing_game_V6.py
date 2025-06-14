"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
# When the program starts, we want to:
# ------------------------------------
# 1. Display an intro/welcome message to the player.X
# 2. Store a random number as the answer/solution.X
# 3. Continuously prompt the player for a guess.X
#   a. If the guess is greater than the solution, display to the player "It's lower".X
#   b. If the guess is less than the solution, display to the player "It's higher".X
# 4. Once the guess is correct, stop looping, inform the user they "Got it"X
#    and show how many attempts it took them to get the correct number.X
# 5. Let the player know the game is ending, or something that indicates the game is over.X
#   (You can add more features/enhancements if you'd like to.)
#
# XKick off the program by calling the start_game function.
# XCreate the start_game function.
# XTODO: Put anything with potential error problems in try blocks
# XTODO: Raise error when number entered is lower than lowest_num or higher than highest_num. Tell the user the number is outside the valid range
# XTODO: handle ValueError for when a number isn't entered in guess field.
# Make it so that if the user re guesses a number that it tells them they have already entered that number
# XTODO: Make sure that is user enters a value other than y or n for play_again that the error is handled
# XTODO: Create a way to save the lowest number of guesses as the highscore while the program is running
# XTODO: handle floats error
# TODO: if you enter -0 print easter egg message "You're silly, -0 doesn't exist! Or does it?"
# XTODO: fix issue where is neither y or n only are entered that the code ends abruptly
# XTODO: fix issue where after the user enters a number outside the range and the enters another number outside the range that the outside range message doesn't display
# Handle Errors from when value entered isn't able to be used with .lower
# XImport the random module.

#import sys
import random

# Change game number range here.
lowest_num = 1
highest_num = 10
dividing_line = "-" * 40

# Function to Determine the Best Score
def check_score(score, best_score):
    if best_score is None:
        best_score = score
    elif score < best_score:
        best_score = score
    return best_score

# Game
def start_game(best_score):
    generated_number = random.randint(lowest_num, highest_num)
    attempt_count = 0
    player_guess = None
    while player_guess != generated_number:
        attempt_count += 1
        try:
            player_guess = int(input(f"Guess an integer within the range of {lowest_num} through {highest_num}: "))
            if player_guess < lowest_num or player_guess > highest_num:
                print(f"This number is outside the guessing range.")
            else:
                if player_guess < generated_number:
                    print(f"The correct number is higher than {player_guess}.")
                if player_guess > generated_number:
                    print(f"The correct number is lower than {player_guess}.")
        except ValueError:
            print("Sorry, you didn't enter a whole number.")
    print(f"You got it! The correct number was {generated_number}! \n"
          f"You guessed in {attempt_count} tries. \n")
    current_best_score = check_score(attempt_count, best_score)
    play_again = input(f"Would you like to play again? [y]es/[n]o: ")
    choice_play_again(play_again, current_best_score)

# Function to allow the player the choice to play again and display their best score
def choice_play_again(choice, score):
    while choice.lower() != "y" or "n":
        if choice.lower() == "y":
            print(f"The Best Score is {score}")
            start_game(score)
            # Break Included to Communicate end of the While Loop. Not Necessary for Code to Function.
            break
        elif choice.lower() == "n":
            print(f"Closing Game. Thank you for playing! Your Best Score was {score}!")
            break
        else:
            choice = input(f"Sorry, I didn't understand that. Try again [y]es/[n]o: ")

# Welcome Message
print(dividing_line + "\nWelcome to Guess the Number!\n" + dividing_line)
# Start the Game
start_game(None)