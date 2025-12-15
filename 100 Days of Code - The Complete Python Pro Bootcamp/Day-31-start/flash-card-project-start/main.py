from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

box = Tk()
box.title("Flashy")
box.config(padx=50, pady=50, background=BACKGROUND_COLOR)

box_canvas = Canvas(height=600, width=900)
ft_card = PhotoImage(file="./images/card_front.png")
box_canvas.create_image(263, 400, image=ft_card)
box_canvas.grid(row=0, column=0)

right = PhotoImage(file="./images/right.png")
right_button = Button(image=right)

box.mainloop()