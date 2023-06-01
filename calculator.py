from tkinter import *

#### Functions ####

#Addition
def add(n1, n2):
    return n1 + n2


#Subtraction
def subtract(n1, n2):
    return n1 - n2


#Multiplication
def multiply(n1, n2):
    return n1 * n2


#Division
def divide(n1, n2):
    return n1 / n2

# Change sign of a number
def change_sign(n1):
    return (n1*(-1))

# Return number in percent
def percent(n1):
    return (n1 / 100)

# TODO: add function to equal button
def calculate():
    pass

# TODO: add function to AC button
def reset():
    pass

# TODO: add function to comma button
def comma():
    pass

#### Interface ####
screen = Tk()
screen.minsize(600,700)
screen.title("Basic GUI Calculator")

# Label for result
result_label = Label(text="0")
result_label.grid(column=0, row=0)

# First row of buttons
ac_button = Button(text="AC")
ac_button.grid(column=0, row=1)

change_sign_button = Button(text="+/-", command=change_sign)
change_sign_button.grid(column=1, row=1)

percent_button = Button(text="%", command=percent)
percent_button.grid(column=2, row=1)

devide_button = Button(text="/", command=divide)
devide_button.grid(column=3, row=1)


# Second row of buttons 
seven_button = Button(text="7")
seven_button.grid(column=0, row=2)

eight_button = Button(text="8")
eight_button.grid(column=1, row=2)

nine_button = Button(text="9")
nine_button.grid(column=2, row=2)

multiply_button = Button(text="x", command=multiply)
multiply_button.grid(column=3, row=2)

# Third row of buttons 
four_button = Button(text="4")
four_button.grid(column=0, row=3)

five_button = Button(text="5")
five_button.grid(column=1, row=3)

six_button = Button(text="6")
six_button.grid(column=2, row=3)

minus_button = Button(text="-", command=subtract)
minus_button.grid(column=3, row=3)

# Fourth row of buttons 
one_button = Button(text="1")
one_button.grid(column=0, row=4)

two_button = Button(text="2")
two_button.grid(column=1, row=4)

three_button = Button(text="3")
three_button.grid(column=2, row=4)

add_button = Button(text="+", command=add)
add_button.grid(column=3, row=4)

# Fifth row of buttons 
zero_button = Button(text="0")
zero_button.grid(column=0, row=5)

comma_button = Button(text=",")
comma_button.grid(column=1, row=5)

equal_button = Button(text="=")
equal_button.grid(column=3, row=5)


#possible operations to work with, saved in a dictionary
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


#########function for calculation#########
def calculation():
    #variable to end program
    exit = False
    num1 = float(input("Enter first number: "))
    #loop through the dictionary of operations to offer symbols to user
    for operator in operations:
        print(operator)
    while not exit:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))
        #calculate result
        operation_function = operations[operation_symbol]
        answer = operation_function(num1, num2)
        #print answer
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        end_program = input(
            f"Type 'y' to continue calculation with {answer} or 'n' to start a new calculation: "
        ).lower()
        #check if program should be ended after calculation
        if end_program == "y":
            #set num1 to answer to continue calculating
            num1 = answer
        else:
            exit = True
            print(f"The end result is {answer}.")
            calculation()


calculation()
