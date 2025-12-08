from tkinter import *
import random
from char import letters, numbers, symbols
FONT = ("Arial", 12)

PASSWORD_LENGTH = 12

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    char_options = []
    all_chars = letters, numbers, symbols
    char_list = char_options.append(random.choice(all_chars))
    for each in range(all_chars):


    random.shuffle(char_options)
    make_password = "".join(char_options)
    return make_password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    password = password_input.get()
    user = user_input.get()

    with open("data.txt", "a") as df:
        df.write(f"{website} | {user} | {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.grid_columnconfigure(1, weight=1)


canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=1)

#website row
web_text = Label(text="Website: ", font=FONT)
web_text.grid(column=0, row=2, sticky="w")

website_input = Entry(width=43)
website_input.grid(column=1, row=2, columnspan=2, sticky="w")
website_input.focus()

#email/username
user_label = Label(text="Email/Username: ", font=FONT)
user_label.grid(column=0, row=3, sticky="w")
user_input = Entry(width=43)
user_input.grid(column=1, row=3, columnspan=2, sticky="w")
user_input.insert(0, "taeyeon@email.com")

#password
password_label = Label(text="Password: ", font=FONT)
password_label.grid(column=0, row=4, sticky="w")
password_input = Entry(width=21)
password_input.grid(column=1, row=4, sticky="w")

#button generate password
new_pass_button = Button(text="Generate Password", command=generate_password)
new_pass_button.grid(column=2, row=4)

#add button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=5, sticky="w",columnspan=2)






window.mainloop()