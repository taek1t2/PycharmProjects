from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

box = Tk()
box.title("Flashy")
box.config(padx=50, pady=50, background=BACKGROUND_COLOR)

box_canvas = Canvas(height=600, width=900)
ft_card = PhotoImage(file="./images/card_front.png")
box_canvas.create_image(450, 300, image=ft_card)
box_canvas.grid(row=0, column=0)

right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, background=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(row=1, column=1, columnspan=1)

wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, background=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(row=1, column=0, columnspan=1)


card_font =


box.mainloop()