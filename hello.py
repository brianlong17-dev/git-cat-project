import random
import string
import tkinter as tk
from tkinter import messagebox
print("hello world")
name = "Brian"
# No changes needed to this section

def randomName():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    return random.choice(names)

randomNameL = lambda: random.choice(["Johny", "Saraho", "Mikey", "Emma", "David"])


name = randomName()
printString = ("hello world", randomNameL())
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Dialog", f"{printString[0]} - {printString[1]}")
root.destroy()
print(f"Dialog: {printString[0]} - {printString[1]}")