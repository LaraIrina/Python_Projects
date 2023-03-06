import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
else:
  print(scissors)

print(f"Computer chose {computer_choice}:")
if computer_choice == 0:
  print(rock)
  if choice == computer_choice:
    print("Draw, try again.")
  elif choice == 1 and computer_choice == 0:
    print("You won.")
  else:
    print("Computer won.")
elif computer_choice == 1:
  print(paper)
  if choice == computer_choice:
    print("Draw, try again.")
  elif choice == 0 and computer_choice == 1:
    print("Computer won.")
  else:
    print("You won.")
else:
  print(scissors)
  if choice == computer_choice:
    print("Draw, try again.")
  elif choice == 0 and computer_choice == 2:
    print("You won.")
  else:
    print("Computer won.")