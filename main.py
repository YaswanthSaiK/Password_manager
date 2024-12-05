from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def passw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list + [random.choice(symbols) for i in range(nr_symbols)]
    password_list + [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    input3.insert(0, password)
    pyperclip.copy(password)
def copypass():
    input3.delete(0, END)
    passw()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new1 = input1.get()
    new2 = input2.get()
    new3 = input3.get()
    new_data = {
        new1 : {
            "email": new2,
            "password": new3
        }
    }
    if len(new1) != 0 and len(new3) != 0:
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)
                data.update(new_data)
        except FileNotFoundError:
            f = open("data.json", "w")
            json.dump(new_data, f, indent=4)
        else:
            with open("data.json", "w") as datafile:
                json.dump(data, datafile, indent=4)

        finally:
            input1.delete(0, END)
            input3.delete(0, END)
    else:
        messagebox.showwarning(title="fill up!!!", message="Dont leave any fields empty!!")
def findpass():
    new1 = input1.get()
    try:
        with open("data.json", "r") as datafile:
            data3 = json.load(datafile)
            try:
                for i in range(0, len(data3)):
                    messagebox.askokcancel(title="credentials", message=f"email:{data3[new1]['email']} \n"
                                                                             f"Password:{data3[new1]['password']}")
                    break
            except:
                messagebox.showwarning(title="No details", message="No details for this website exists")
    except FileNotFoundError:
        messagebox.showwarning(title="File not found", message="Sorry!, file was not found.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("my password manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
pic = PhotoImage(file="logo.png")
canvas.create_image(110, 110, image=pic)
canvas.grid(column=1, row=0)

web = Label(text="Website:", font=("ariel", 14, "bold"))
web.grid(column=0, row=1)
email = Label(text="Email/Username:", font=("ariel", 14, "bold"))
email.grid(column=0, row=2)
password = Label(text="Password:", font=("ariel", 14, "bold"))
password.grid(column=0, row=3)

input1 = Entry(width=35)
input1.grid(column=1, row=1)
input1.focus()
input2 = Entry(width=54)
input2.grid(column=1, row=2, columnspan=2)
input2.insert(0, "yaswanthsaikillampudi@gmail.com")
input3 = Entry(width=35)
input3.grid(column=1, row=3)

button1 = Button(text="Generate Password", command=copypass)
button1.grid(column=2, row=3)
button2 = Button(text="Add", width=48, command=save)
button2.grid(column=1, row=4, columnspan=2)
search = Button(text="Search", width=14,  command=findpass)
search.grid(row=1,column=2)

window.mainloop()

