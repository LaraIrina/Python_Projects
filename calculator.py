#This code creates a calculator in python
##########################################
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


#possible operations to work with, saved in a dictionary
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


#########function for calculation#########
def calculation():
    #variable to end program
    exit = False
    num1 = int(input("Enter first number: "))
    #loop through the dictionary of operations to offer symbols to user
    for operator in operations:
        print(operator)
    while not exit:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number: "))
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
