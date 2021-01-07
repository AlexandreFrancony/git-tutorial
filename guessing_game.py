#! /usr/bin/python3
 
# The random package is needed to choose a random number
import random
import os
import time
 
# Define the game in a function
print("Hello dear player! How should I call you?\nYour nickname : ", end="")
pseudo = input()
def guess_loop():
    # This is the number the user will have to guess, chosen randomly in between 1 and 100
    number_to_guess = random.randint(1, 100)
    print("I have in mind a number in between 1 and 100, can you find it?")
 
    # Replay the question until the user finds the correct number
    while True:
        try:
            # Read the number the user inputs
            guess = int(input())
 
            # Compare it to the number to guess
            if guess > number_to_guess:
                print("The number to guess is lower")
            elif guess < number_to_guess:
                print("The number to guess is higher")
            else:
                # The user found the number to guess, let's exit
                print("You just found the number, it was indeed", guess)
                return
        # A ValueError is raised by the int() function if the user inputs something else than a number
        except ValueError as err:
            print("Invalid input, please enter an integer")
 


#Speech initialised
def speech(pseudo):
	print("Bien joué ", end="")
	print(pseudo, end=" ")
	print("! You just won!", end="\n")
	input("( Press enter to continue... ↲ )")
	os.system('clear')
	input("Hello! I'm M.A.T.I.S., a bot created by the group you are actually gradding. ↲ \n")
	input("Alexandre gave me the mission to reward you for doing such an achievement, not everyone can win the guessing_game.py! ↲ \n")
	input("But what can I award you? You just played a game, made by a Unix teacher, that Alexandre just copy-pasted here! ↲ \n")
	input("Yes, I know, you truely didn't win any physical thing or award like this.↲ \n")
	input("But you made Alexandre learn a lot! Using GitHub, fooling around with the terminal, he clearly enjoyed himself! ↲ \n")
	input("So i can at least declare on behalf of his whole team : Thanks a lot for learning us how to use a UNIX system! ↲ \n")
	print("Now this program is gonna close itself in 5 seconds, thanks a lot!\n")
	time.sleep(1)
	print("5 \n")
	time.sleep(1)
	print("4 \n")
	time.sleep(1)
	print("3 \n")
	time.sleep(1)
	print("2 \n")
	time.sleep(1)
	print("1 \n")
	time.sleep(1)
	os.system('clear')

#Launch the game
if "win" in pseudo :
	speech(pseudo)

else :
	guess_loop()
	speech(pseudo)

