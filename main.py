import sys
import tkinter as tk
from tkinter import *
from info import Game_Title
import Game



root = tk.Tk()

def play():
    Game.play()
    sys.exit()

def close():
    sys.exit()
root.title(Game_Title + " " + "Launcher")
display = Canvas(root, height=400, width=500, bg= "#263D42")
display.grid(columnspan=1000, rowspan=1000)

button1 = tk.Button(root, text="Play", bg="#263D42", fg="#00FFFF", command=play)
button1.grid(column=500, row=490)

button2 = tk.Button(root, text="Close", bg="#263D42", fg="#00FFFF", command=close)
button2.grid(column=500, row=500)

root.mainloop()