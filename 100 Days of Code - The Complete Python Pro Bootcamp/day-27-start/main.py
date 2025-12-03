from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=400, height=300)

#label
my_label = Label(text="Some Text", font=("Arial", 24, "bold"))
my_label.config(text="new text")
# my_label.pack(side="left")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

#button
button = Button(text="Click Me", command=button_clicked)
# button.pack(side="left")
button.grid(column=1, row=1)
new_button = Button(text="Click the 2nd Me")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=20)
# input.pack(side="left")
input.grid(column=3, row=2)
input.get()

#Text

#Spinbox

#Scale

#Checkbutton

#Radiobutton

#Listbox






window.mainloop()