#Number Guessing Game:
##### Imports #####
import art
import random
from replit import clear

#### Functions ####
def guessing_game():
  end_game = False
  #creates a list of numbers in a given range
  def create_list_of_answers(start, end):
      return list(range(start, end))
  #chooses a random number of list between 1 and 100
  def generate_random_number():
    answer = random.choice(create_list_of_answers(1,100))
    return answer

  #### Game Code ####
  print(art.logo)
  print("Welcome to the Number Guessing Game!\nI think of a number between 1 and 100.")
  
  answer = generate_random_number()
  #print(answer)
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    lives = 10
  elif difficulty == "hard":
    lives = 5
  
  while lives > 0 and end_game == False:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    if guess == answer:
      end_game = True
      print(f"Congratulations, you guessed the correct number.\n{art.win}")
  
    
    elif guess > answer:
      print("Too high.")
      lives -= 1
    
    elif guess < answer:
      print("Too low.")
      lives -= 1
    
  if lives == 0:
    print(f"You ran out of lives.\n{art.lose}")
    print(f"The correct answer is {answer}.")
  restart = input("Would you like to play again? y/n: ").lower()
  if restart == "y":
    clear()
    guessing_game()
  elif restart == "n":
    print("Okay, can't wait to beat you again. Bye bye!")

#start game
guessing_game()

