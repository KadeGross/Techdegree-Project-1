"""
Python Development Techdegree
Project 1 - The Number Guessing Game
Kade Gross
--------------------------------
"""
# Imported Random Module to Generate a Number for the Game
import random

# Change game number range here.
# This allows anyone to adjust the difficulty of the game easily.
lowest_num = 1
highest_num = 10
dividing_line = "-" * 40

# Main Game Code:
# Here the user is prompted for their guess.
# Their guess is compared to the random number generated within the range specified above.
# If the user entered number does not equal the generated number, the while loop continues
# to compare guesses to the generated number.
# If the correct number is either higher or lower than the guessing range
# the user is told to guess a number withing the specified range.
# If the user guess is withing the number range and is an integer
# but is not equal to the generated number the game logic will inform the user
# if the correct number is higher or lower than their guess.
def start_game(best_score):
    generated_number = random.randint(lowest_num, highest_num)
    attempt_count = 0
    player_guess = None
    while player_guess != generated_number:
        attempt_count += 1
        try:
            player_guess = int(input(f"Guess an integer within the range of {lowest_num} through {highest_num}: "))
            if player_guess == -0:
                print("You're silly, -0 doesn't exist! Or does it?")
            elif player_guess < lowest_num or player_guess > highest_num:
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


# Function to Determine the Best Score:
# (I use the term best score because I believe it's more appropriate in this game.
# I hope it's not an issue for grading. If it is I have no issue changing the terminology and resubmitting.)
# This function compares the score from the previous game to the score from the
# most recent game and returns the higher of the two scores.
def check_score(score, best_score):
    if best_score is None:
        best_score = score
    elif score < best_score:
        best_score = score
    return best_score


# Function to allow the player the choice to play again and display their best score.
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

# Display a Welcome Message to the Player
print(dividing_line + "\nWelcome to Guess the Number!\n" + dividing_line)

# Call Function to Start the Game
start_game(None)