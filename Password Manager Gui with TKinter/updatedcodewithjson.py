from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip # A Module to copy and paste clipboard
import json

def generate_password():
    letters = ['a','b','c','d','e','f','g','h','i','j']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']



    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]


    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)




def save():
    website = Website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            'email': email,
            'password': password,
            }}
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = 'Oops', message = 'Please make sure you haven\'t left any fields empty')
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)   
        except FileNotFoundError:
            with open('data.json','w') as data_file:                            
                json.dump(new_data, data_file, indent = 4)                  
        else:
            # Updating old data with new data
            data.update(new_data)
            
            
            with open('data.json','w') as data_file:
                json.dump(data, data_file, indent = 4)
        finally:
            Website_entry.delete(0, END)
            password_entry.delete(0, END)
            
    


# UI Setup

window = Tk()
window.title('Password Manager')
window.config(padx = 50, pady = 50)


canvas = Canvas(height = 200, width = 200)
logo_img = PhotoImage(file = 'logo.png')
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column = 1)

# Labels
website_label = Label(text = 'Website :')
website_label.grid(row = 1, column = 0)

email_label = Label(text = 'Email/Username :')
email_label.grid(row = 2, column = 0)

password_label = Label(text = 'Password :')
password_label.grid(row = 3, column = 0)

# Entries
Website_entry = Entry(width = 35)
Website_entry.grid(row = 1, column = 1, columnspan = 2)
Website_entry.focus()

email_entry = Entry(width = 35)
email_entry.grid(row = 2, column = 1, columnspan = 2)
email_entry.insert(0, 'angela123@gmail.com')

password_entry = Entry(width = 35)
password_entry.grid(row = 3, column = 1, columnspan = 2)

# Buttons
generate_password_button = Button(text = 'Generate Password', command = generate_password)
generate_password_button.grid(row = 3, column = 2)

add_button = Button(text = 'Add', width = 30,command = save) # Radiobutton is a type of widget that allows you to choose only one option from a group of options
add_button.grid(row = 4, column = 1, columnspan = 2)












window.mainloop()