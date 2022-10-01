import tkinter as tk
from tkinter import ANCHOR, CENTER, Button, Entry, Label, filedialog, Text
import os
import BrokenGameCopy as bkg

root = tk.Tk()
root.title("Welcome to Game of Game")
root.geometry('500x500')

# canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# canvas.pack()

# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8)   
def clicked():
    None

btn = Button(root, text = "Enter" ,fg = "black", command=clicked , width=25)
btn.place(relx=0.5, rely=0.5, anchor='center')

text = tk.Text(root)
text.grid_size(3,9)


text.pack()


root.mainloop()

