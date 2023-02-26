
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200*2, height=224*2, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
image_shift = 2
# canvas.create_image(100 + image_shift,112, image = tomato_img )
canvas.create_image(200,223, image = tomato_img )
canvas.create_text(200, 240, text="00:00", fill = "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start",highlightthickness=0,font=(FONT_NAME, 18, "bold"))
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset",highlightthickness=0,font=(FONT_NAME, 16, "bold"))
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW,font=(FONT_NAME, 24, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
