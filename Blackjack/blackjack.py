#### Imports
import random
from replit import clear
import art

def play_blackjack():
  #### Preconditions
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  score = 0
  game_over = False
  
  #### Functions
  def get_card():
    card = random.choice(cards)
    return card
  
  #detect a blackjack (Ace + 10)
  def has_blackjack(hand):
    if hand == [10, 11] or hand == [11, 10]:
      return True
      
  # calculate score of hand
  def get_score(hand):
    score = 0
    for i in range(len(hand)):
      score += hand[i]
      if 11 in hand:
        if score > 21:
          for i in range(len(hand)-1):
            if hand[i] == 11:
              hand[i] -= 10
    return score
  
  # print the current hand
  def show_hand(hand, score):
    score = get_score(hand)
    print(f"The current hand looks like: {hand} and the score is: {score}.")
    
  #checks who won
  def check_winner(user_score, user_hand, dealer_score, dealer_hand):
    if dealer_score > 21:
      print(f"You win!\nYour hand is {user_hand} and your score is {user_score}, the dealer's hand looks like {dealer_hand} and the dealer score is {dealer_score}.")
    elif user_score == dealer_score:
      print(f"It's a draw!\nYour hand is {user_hand} and your score is {user_score}, the dealer's hand looks like {dealer_hand} and the dealer score is {dealer_score}.")
    elif user_score < dealer_score:
      print(f"You lose!\nYour hand is {user_hand} and your score is {user_score}, the dealer's hand looks like {dealer_hand} and the dealer score is {dealer_score}.")
    else:
      print(f"You win!\nYour hand is {user_hand} and your score is {user_score}, the dealer's hand looks like {dealer_hand} and the dealer's score is {dealer_score}.")
  
  def check_score(score):
    if score > 21:
      game_over = True
      print(f"Your score is {score} and you lose.")
      
##########################  
########## Game ##########
##########################
  print(art.logo)
  print("Welcome to Blackjack. You and the dealer will now get two cards each as your starting hand. You win this game with a black jack (a score of 21) or when your end-score is higher than the dealer's score. You begin: ")
  
  #create starting hands of 2 random card values
  user_hand = []
  dealer_hand = []
  for i in range (2):
    user_hand.append(get_card())
    dealer_hand.append(get_card())
  
  #detect if user or dealer has a blackjack
  if has_blackjack(user_hand) == True:
    game_over = True
    print("You win with a blackjack!")
  elif has_blackjack(dealer_hand) == True:
    game_over = True
    print("The dealer wins with a blackjack!")
  
  #get current scores  
  user_score = get_score(user_hand)
  check_score(user_score)
  show_hand(user_hand, score)
  dealer_score = get_score(dealer_hand)
  
  #reveal dealers first card to user
  print(f"Dealer's first card: {dealer_hand[0]}")
  
  #Game ends when user score goes over 21 or one of the players gets a blackjack
  while not game_over:
    another_card = input("Would you like to get another card? y/n: \n").lower()
    
    #user wants another card
    if another_card == 'y':
      user_hand.append(get_card())
      user_score = get_score(user_hand)
      check_score(user_score)
      show_hand(user_hand, score)

      if get_score(user_hand) >= 21:
          game_over = True
        
    #user is done and lets the dealer play
    elif another_card == 'n':
      print("The dealer is currently drawing the cards...")
      while dealer_score < 16 and game_over == False:
        dealer_hand.append(get_card())
        dealer_score = get_score(dealer_hand)
        show_hand(dealer_hand, score)

        if get_score(dealer_hand) >= 21 :
          game_over =  True
        
      #set game_over after finishing the while loop to end game
      game_over = True
      check_winner(user_score, user_hand, dealer_score, dealer_hand)
  ask_user_to_play_again = input("Would you like to play again? y/n\n").lower()
  if ask_user_to_play_again == 'n':
    print("Ok, bye bye!")
  elif ask_user_to_play_again == 'y':
    clear()
    play_blackjack()

    #start the game
play_blackjack()