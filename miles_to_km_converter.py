from tkinter import *

def calculate():
    miles = float(input_miles.get())
    km = miles * 1.60934
    second_line_text2.config(text=km)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50,pady=50)

#Entry
input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

#Label: Miles
first_line_text = Label(text="Miles")
first_line_text.grid(column=2, row=0)

#Label: is equal to _ Km
second_line_text1 = Label(text= "is equal to ")
second_line_text1.grid(column=0, row=1)

#Label: is equal to _ Km
second_line_text2 = Label(text= "0")
second_line_text2.grid(column=1, row=1)

#Label: is equal to _ Km
second_line_text3 = Label(text= " Km")
second_line_text3.grid(column=2, row=1)

#Button to start calculation
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

#keep window open 
window.mainloop()