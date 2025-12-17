import csv
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT= ("Arial", 35, "italic")
WORD_FONT = ("Arial", 55, "bold")

data = pandas.read_csv("./data/french_words.csv")
df = data.to_dict("records")

def next_card():
    current_card = random.choice(df)
    box_canvas.itemconfig(card_title, text="French")
    box_canvas.itemconfig(card_word, text=current_card["French"])

box = Tk()
box.title("Flashy")
box.config(padx=50, pady=50, background=BACKGROUND_COLOR)

box_canvas = Canvas(width=900, height=700, bg=BACKGROUND_COLOR, highlightthickness=0)
ft_card = PhotoImage(file="./images/card_front.png")
box_canvas.create_image(450, 275, image=ft_card)
box_canvas.grid(row=0, column=1)
card_title = box_canvas.create_text(450, 150, text="", font=FONT, fill="black")
card_word = box_canvas.create_text(450, 300, text="", font=WORD_FONT, fill="black")


right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, background=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right_button.place(relx=0.5, rely=1.0, x=140, y=-20, anchor="s")

wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, background=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.place(relx=0.5, rely=1.0, x=-140, y=-20, anchor="s")


next_card()

box.mainloop()