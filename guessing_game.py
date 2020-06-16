# Guessing Game - Week 3
# Knowledge about for loop, while loop, if/eval
import random
print("Let's play a Guessing Game!")
print("I am thinking of a number from 1-100 (inclusive)")
my_num = random.randint(1,100)
guessed_num = input("Give a guess on the number I am thinking of! : ")
guessed_num = int(guessed_num)
guesses = 0

while ((guessed_num != my_num) and guesses < 10):
  guesses += 1
  print("You have " + str(10 - guesses) + " guesses left!")
  guessed_num = int(guessed_num)
  if(guessed_num > 100 or guessed_num < 1):
    guessed_num = input("Please guess a number within 1-100 (inclusive): ")
  elif(guessed_num < my_num):
    guessed_num = input("Your quess is too low! Try again: ")
  elif(guessed_num > my_num):
    guessed_num = input("Your quess is too high! Try again: ")

if(guessed_num != my_num and guesses == 10):
  print("You ran out of guesses! My number was " + str(my_num) + ". GAME OVER! YOU ARE A LOSER!")
if (guessed_num == my_num):
  print("You got it right! " + str(my_num) + " is my number - YOU WIN!")

