from tkinter import *
from tkinter import messagebox
import random
from char import letters, numbers, symbols
FONT = ("Arial", 12)

PASSWORD_LENGTH = 16

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    temp_password_list = []
    all_chars = letters + numbers + symbols
    print(all_chars)
    for _ in range(PASSWORD_LENGTH):
        random_letter = random.choice(all_chars)
        temp_password_list.append(random_letter)

    random.shuffle(temp_password_list)
    make_password = "".join(temp_password_list)
    password_input.insert(0, make_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    password = password_input.get()
    user = user_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: Email: {user} \n "
                                                              f"Password: {password} \n Is it ok to save?")

    if is_ok:
        with open("data.txt", "a") as df:
            df.write(f"{website} | {user} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0,END)


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