from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, END)
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    formatted_string = f"{website} | {username} | {password}\n"

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showwarning(title="Error", message="You need to complete all fields")
    else:
        is_confirmed = messagebox.askokcancel(title=website, message=f"There are the details entered: \n"
                                                      f"Email: {username} \n Password: {password}")
        if is_confirmed:
            with open("password_data.csv", mode="a") as data_file:
                data_file.write(formatted_string)
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #


# Set up window
window = Tk()
window.title("Password Generator")
window.config(pady=50, padx=50, width=200, height=200)

# Set up Canvas/Image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Website Label/Input
website_label = Label(text="Website:", pady=5)
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username Input
username_label = Label(text="Email/Username:", pady=5)
username_label.grid(column=0, row=2)
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, "anthony.bar.89@gmail.com")

# Password Input
password_label = Label(text="Password:", pady=5)
password_label.grid(column=0, row=3)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=33, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)




window.mainloop()