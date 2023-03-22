#Import the required library
from tkinter import *
import tkinter as tk
import OnePlayers

def lose():
#Create an instance of tkinter frame
    app = tk.Tk()
    def show_module():
    # Create an instance of module2 and start its event loop
        module2_app = OnePlayers.OnePlayers()
        module2_app.mainloop()
    #Set the geometry
    app.geometry("1500x1000")

    #Create a canvas object
    canvas= Canvas(app, width= 1000, height= 750, bg="pink")

    #Add a text in Canvas
    canvas.create_text(550, 350, text="SORRY,YOU LOST!", fill="black", font=('Helvetica 50 bold'))
    canvas.pack()
    button = tk.Button(app, text="Try Again!", command=show_module)
    button.pack()

    app.mainloop()