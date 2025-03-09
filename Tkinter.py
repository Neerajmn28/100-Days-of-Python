import tkinter 

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width = 500, height = 300)
window.config(padx = 20, pady = 20)


# Label
my_label = tkinter.Label(text = 'I am a Label', font = ('Arial',24,'bold'))
my_label.pack() # To place the 'I am a Label' on to the screen

# This is how we change the existing label
my_label['text'] = 'New Text' 
my_label.config(text = 'New Text')
my_label.place(x = 0, y = 0)
my_label.grid(column = 0, rows = 5)



# Button
def button_clicked():
    print('I got clicked')
    new_text = input.get()
    my_label.config(text = new_text )
    

button = tkinter.Button(text = 'Click Me', command = button_clicked )
button.pack()

# Entry
input = tkinter.Entry(width = 10)
input.pack()
print(input.get())







window.mainloop() # Will keep the window running