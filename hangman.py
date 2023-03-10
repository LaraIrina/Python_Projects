import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
      lives -= 1
    if guess in display:
      print("You already guessed this letter.")
        
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(stages[lives])

    #Join all the elements in the list and turn it into a String.
    if lives > 0:
      print(f"{' '.join(display)}")
    else:
      print("You lost.")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

