from tkinter import *

FONT = ("Arial", 13)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=100)
window.config(padx=20, pady=20)
window.columnconfigure(1, weight=1)
# window.rowconfigure(0, weight=1)


equal_to_label = Label(text="Is Equal To", font=FONT)
equal_to_label.grid(column=0, row=1)

miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)

input = Entry(width=20)
input.grid(column=1, row=0)
input.get()

calculate = Button(text="Calculate")
calculate.grid(column=1, row=2)

kilom_result_label = Label(text="0")
kilom_result_label.grid(column=1, row=1)

kilom_label = Label(text="Km", font=FONT)
kilom_label.grid(column=2, row=1)

window.mainloop()