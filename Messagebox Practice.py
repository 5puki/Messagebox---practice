from tkinter import *
from tkinter import messagebox

def click():
    practice = messagebox.askyesnocancel(title = "Practice", message = "Do you like to practice?")
    if practice == True:
        print("You like to practice! :)")
    elif practice == False:
        print("You don't like to practice :/")
    else:
        print("Do not dodge the question!")

window = Tk()

button = Button(window,
                text = "click here!",
                command = click)
button.pack()

window.mainloop()