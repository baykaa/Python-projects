# Creating a Calculator GUI
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# Event handler for button click:
def button_add():
    number = int(entry.get())
    number2 = int(entry2.get())
    result = number + number2 
    messagebox.showinfo(f"Result: {result}", f"Result: {result}")

def button_subtract():
    number = int(entry.get())
    number2 = int(entry2.get())
    result = number - number2 
    messagebox.showinfo(f"Result: {result}", f"Result: {result}")

def button_multiply():
    number = int(entry.get())
    number2 = int(entry2.get())
    result = number * number2 
    messagebox.showinfo(f"Result: {result}", f"Result: {result}")

def button_divide():
    number = int(entry.get())
    number2 = int(entry2.get())
    result = number / number2 
    messagebox.showinfo(f"Result: {result}", f"Result: {result}")

# Create an Entry widget:
entry = tk.Entry(root)
entry.pack()

# Create a second Entry widget:
entry2 = tk.Entry(root)
entry2.pack()

# Create a Button widget:
buttonAdd = tk.Button(root, text="Add", command=button_add)
buttonAdd.pack()

buttonSubtract = tk.Button(root, text="Minus", command=button_subtract)
buttonSubtract.pack()

buttonMultiply = tk.Button(root, text="Multiply", command=button_multiply)
buttonMultiply.pack()

buttonDivide = tk.Button(root, text="Divide", command=button_divide)
buttonDivide.pack()

root.mainloop()