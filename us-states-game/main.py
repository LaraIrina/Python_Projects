import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

#load in image as shape of screen 
image = "blank_states_img.gif"
screen.addshape(image)
#once shape is added its usable as shape of turtle
turtle.shape(image)
#get list of states from csv file using pandas
data = pandas.read_csv("50_states.csv")
states_list = data.state.tolist()
guessed_states = []
    
while len(guessed_states) < 50:
    #pop up to ask user for states names 
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt = "What is another state's name?").title()

    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state) 
    elif answer_state == "Exit":
        #creates a csv file with states that have not been guessed
        not_guessed_states = []
        for state in states_list:
            if state not in guessed_states:
                not_guessed_states.append(state)
        new_data_frame = pandas.DataFrame(not_guessed_states)
        new_data_frame.to_csv("states_to_learn.csv")
        break




