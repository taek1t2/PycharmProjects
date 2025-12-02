from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=400, height=300)

#label
my_label = Label(text="Some Text", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "new text"
my_label.config(text="new text")

#button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = Entry(width=20)
input.pack()
input.get()





window.mainloop()