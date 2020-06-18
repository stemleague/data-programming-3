#### GUESSING GAME ASSIGNMENT ####
# Hello Developers! Today we are going to make a Guessing Game! 
# How the Guessing Game works is that you want to use the random number generator in python by importing random:
import random 
# also, you want to use the random.randint(a, b) method in python. Essentially, this will return a random integer N such that a <= N <= b (range from a to b).
# Since we want to let the user pick the range of the number to be guessed, we can use the input() function. For example, if we want the user to guess numbers from 1 to 100, then we can do:
generated_num = int(input("Give a guess on the number I am thinking of! : ")) # remember to cast the user's input to an integer!
guessed_num = random.randint(1, 100)
guesses = 0 # Since the user has not used any of their guesses yet, it is set to 0

# PART 1: For this lesson, we learned about while loops and since this is a guessing game, we want the user to keep guessing UNTIL they guess the randomly generated number. Therefore, our while loop will need to contain this conditional:
# HINT need a while loop
  # For the conditions inside the loop, we want to inform the user (hint: use if/else loops):
  # 1) If their guessed number is between the range 1-100
  # 2) If their guessed number is less than the generated number
  # 3) If their guessed number is greater than the generated number
  # For each of these cases, we want to inform the user of their guesses and make sure they guess again!
##### YOUR CODE HERE #####













# PART 2: The Guessing Game will end when the user guesses the generated number or the user runs out of guesses. If the user runs out of guesses, then they lose! Display the generated number to the user when the game ends.
##### YOUR CODE HERE #####









# Challenge 1: Try to keep track the number of guesses for the user & update the user how many more guesses they have after each guess. 
##### YOUR CODE HERE #####








# Challenge 2: Change up your variables so that you can allow the user to input the range of the numbers that they would like to guess.
##### YOUR CODE HERE #####









