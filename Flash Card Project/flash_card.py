from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = '#B1DDC6'


current_card = {}
to_learn = {}

try:
    data = pd.read_csv('words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('german words - Sheet1.csv')
    to_learn = original_data.to_dict(orient = 'records')
else:
    to_learn = data.to_dict(orient = 'records') # Each row becomes a dictionary. The column names are the keys.







def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # method used to stop a scheduled event that was previously set using after()
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = 'German', fill = 'black')
    canvas.itemconfig(card_word, text = current_card['German'], fill = 'black')
    canvas.itemconfig(card_background, image = card_front_img)
    flip_timer = window.after(3000, func = show_answer) # execution of the flip_card function after 3,000 milliseconds
    
    
    
def show_answer():
    canvas.itemconfig(card_title, text = 'English', fill = 'white')
    canvas.itemconfig(card_word, text = current_card['English'], fill = 'white')
    canvas.itemconfig(card_background, image = card_back_img)


def got_right():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv('words_to_learn.csv', index = False)


window = Tk()  
window.title('Flash Card')
window.config(padx = 50, pady = 50,bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func = show_answer)
 # execution of the flip_card function after 3,000 milliseconds

canvas = Canvas(width = 800, height = 300)
card_front_img = PhotoImage(file = 'card_front.png')
card_back_img = PhotoImage(file = 'card_back.png')
card_background = canvas.create_image(400, 263, image = card_front_img)
card_title = canvas.create_text(400, 150, text = 'Title', font = ('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text = 'word', font = ('Ariel', 60, 'bold'))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(row = 0, column = 0, columnspan = 2)

# Buttons
cross_image = PhotoImage(file = 'wrong.png')
unknown_button = Button(image = cross_image, highlightthickness = 0, command = next_card)
unknown_button.grid(row = 1, column = 0)

check_image = PhotoImage(file = 'right.png')
known_button = Button(image = check_image, highlightthickness = 0, command = got_right)
known_button.grid(row = 1, column = 1)

next_card()



window.mainloop() 