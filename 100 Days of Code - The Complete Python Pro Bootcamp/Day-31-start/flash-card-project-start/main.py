from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"
FONT= ("Arial", 35, "italic")
WORD_FONT = ("Arial", 55, "bold")





box = Tk()
box.title("Flashy")
box.config(padx=50, pady=50, background=BACKGROUND_COLOR)

box_canvas = Canvas(width=900, height=800, bg=BACKGROUND_COLOR, highlightthickness=0)
ft_card = PhotoImage(file="./images/card_front.png")
box_canvas.create_image(450, 350, image=ft_card)
box_canvas.grid(row=0, column=1)
box_canvas.create_text(450, 250, text="English", font=FONT, fill="black")
box_canvas.create_text(450, 400, text="Word", font=WORD_FONT, fill="black")


right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, background=BACKGROUND_COLOR, highlightthickness=0)
# right_button.grid(row=1, column=1)
right_button.place(relx=0.5, rely=1.0, x=140, y=-20, anchor="s")

wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, background=BACKGROUND_COLOR, highlightthickness=0)
# wrong_button.grid(row=1, column=0)
wrong_button.place(relx=0.5, rely=1.0, x=-140, y=-20, anchor="s")




box.mainloop()