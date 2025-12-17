import csv
from tkinter import *

import pandas
from pandas import *
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT= ("Arial", 35, "italic")
WORD_FONT = ("Arial", 55, "bold")

en_fr_words = pandas.read_csv("./data/french_words.csv")
df = DataFrame.from_dict(en_fr_words)
print(df.to_dict(orient="records"))

box = Tk()
box.title("Flashy")
box.config(padx=50, pady=50, background=BACKGROUND_COLOR)

box_canvas = Canvas(width=900, height=700, bg=BACKGROUND_COLOR, highlightthickness=0)
ft_card = PhotoImage(file="./images/card_front.png")
box_canvas.create_image(450, 275, image=ft_card)
box_canvas.grid(row=0, column=1)
box_canvas.create_text(450, 150, text="English", font=FONT, fill="black")
box_canvas.create_text(450, 300, text="Word", font=WORD_FONT, fill="black")


right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, background=BACKGROUND_COLOR, highlightthickness=0)
right_button.place(relx=0.5, rely=1.0, x=140, y=-20, anchor="s")

wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, background=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.place(relx=0.5, rely=1.0, x=-140, y=-20, anchor="s")




# box.mainloop()