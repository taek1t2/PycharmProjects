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

current_time = 0
timer_running = True
# phase = something
pomodoro_count = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    canvas.itemconfig(timer_label, text=f"{minutes:02d}:{seconds:02d}")
    if total_seconds > 0:
        countdown_starts = window.after(1000, countdown, total_seconds-1)
    else:
        start_time()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

title = Label(text="Timer", fg=RED, bg=YELLOW, font=(FONT_NAME, 45))
title.grid(column=2, row=0, padx=0, pady=20)

check = "🗸"
check_mark = Label(text=check, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
check_mark.grid(column=2, row=4, padx=0, pady=20)

start = Button(text="Start", command=start_time)
start.grid(column=0, row=3)

reset = Button(text="Reset", command=timer_reset)
reset.grid(column=3, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_label = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=2, row=1)


window.mainloop()