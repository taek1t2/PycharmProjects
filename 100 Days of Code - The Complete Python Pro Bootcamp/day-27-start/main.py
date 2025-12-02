import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=400, height=300)

#Label
my_label = tkinter.Label(text= "Label Me", font=("Arial", 24, "bold"))
my_label.pack(side = "left")









window.mainloop()