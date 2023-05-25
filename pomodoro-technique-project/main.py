
# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac" #fg=GREEN for label in green in foreground
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 # variable to keep track of the rounds of work
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0: 
        countdown(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    minutes = math.floor(count / 60)
    seconds = count % 60 
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds }"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        # 1000ms = 1s of wait, function, value to change to
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        checkmarks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW) # adding padding to the tomate image

#create canvas - get color codes from color hunt website
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomate_img = PhotoImage(file="tomato.png") # create image file
canvas.create_image(100,112, image=tomate_img) # x and y coordiantes, image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=YELLOW, font=FONT_NAME, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, font=FONT_NAME, highlightbackground=YELLOW, command= reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(bg=YELLOW)
checkmarks.grid(column=1, row=3)

# keep window open and listening
window.mainloop() 