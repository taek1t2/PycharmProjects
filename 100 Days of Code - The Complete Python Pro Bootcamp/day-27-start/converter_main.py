from tkinter import *

FONT = ("Arial", 13)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=200)
window.config(padx=20, pady=20)
window.columnconfigure(1, weight=1)
# window.rowconfigure(0, weight=1)


equal_to_label = Label(text="Is Equal To", font=FONT)
equal_to_label.grid(column=0, row=3)

miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)

input = Entry(width=20)
input.grid(column=1, row=0)
input.get()

calculate = Button(text="Calculate")


window.mainloop()