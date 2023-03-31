from turtle import Turtle, Screen
import random

is_race_on = False
start_game = True
colors = ["yellow", "orange", "red", "green", "blue", "black"]
screen = Screen()
screen.setup(width=500, height=400)

while start_game:
  #get userbet
  userbet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (yellow/orange/red/green/blue/black): ").lower()
  #create 6 turtles
  all_turtles = []
  for i in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-200, -100 + i*50)
    all_turtles.append(new_turtle)
  
  if userbet:
    is_race_on = True
    
  while is_race_on:
    for turtle in all_turtles:
      #end the game when a turtle reaches the finish line
      if turtle.xcor()>250:
        is_race_on = False
        print(str(turtle.pencolor))
        winner_color = turtle.color()[1]
        if winner_color == userbet:
          play_game = screen.textinput(title="Race is over", prompt=f"Congratulations, the {winner_color} turtle won. Do you want to play again?(y/n): ").lower()
        elif winner_color != userbet:
          play_game = screen.textinput(title="Race is over", prompt=f"Sorry, the {winner_color} turtle won. Do you want to play again?(y/n): ").lower()
        #user wants to play again
        if play_game == "y":
          screen.clear()
        #user doesnt want to play again
        elif play_game == "n":
          start_game = False
        #game is not over, move turtles
      else:
        distance = random.randint(0,10)
        turtle.forward(distance)
  
  #exit game when user clicks the screen
screen.exitonclick()