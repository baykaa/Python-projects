# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()

# Event handler for button click:
# def button_clicked():
#     text = entry.get()
#     print(f"Input: {text}")
#     messagebox.showinfo("Button Clicked!", "Button Clicked!")

# def key_pressed():
#     text = entry.get()
#     messagebox.showinfo(f"Key Pressed: {text}", f"Key Pressed: {text}")

# entry = tk.Entry(root)
# entry.pack()

# button = tk.Button(root, text="Click Me", command=key_pressed)
# button.pack()

# label = tk.Label(root, text="Press any key or click the button")
# label.config(font=("Arial", 20), bg="white", fg="black")
# label.pack()

# root.mainloop()


# EXERCISE 2
# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()

# # Event handler for button click:
# def button_clicked():
#     number = int(entry.get())
#     number2 = int(entry2.get())
#     number3 = int(entry3.get())
#     result = number * number2 * number3
#     messagebox.showinfo(f"Key Pressed: {result}", f"Key Pressed: {result}")

# # Create an Entry widget:
# entry = tk.Entry(root)
# entry.pack()

# # Create a second Entry widget:
# entry2 = tk.Entry(root)
# entry2.pack()

# entry3 = tk.Entry(root)
# entry3.pack()

# # Create a Button widget:
# button = tk.Button(root, text="Calculate", command=button_clicked)
# button.pack()

# root.mainloop()

# EXERCISE -7 
# import tkinter as tk

# root = tk.Tk()

# # Create frames:
# frame1 = tk.Frame(root)
# frame2 = tk.Frame(root)

# # Add widgets to frames:
# label1 = tk.Label(frame1, text="Frame 1")
# label2 = tk.Label(frame2, text="Frame 2")

# label1.pack()
# label2.pack()

# # Pack frames in the main window:
# frame1.pack(side="left")
# frame2.pack(side="right")

# root.mainloop()

# EXERCISE - 8
# import tkinter as tk

# root = tk.Tk()

# # Variable to store checkbox value:
# checkbox_var = tk.IntVar()

# # Event handler for button click:
# def button_clicked():
#     value = checkbox_var.get()
#     if value == 1:
#         print("Checkbox Checked")
#     else:
#         print("Checkbox Unchecked")

# # Create a Checkbox:
# checkbox = tk.Checkbutton(root, text="Check me", variable=checkbox_var)

# # Create a Button widget:
# button = tk.Button(root, text="Submit", command=button_clicked)

# checkbox.pack()
# button.pack()

# root.mainloop()


# step -8 Event handling
# import tkinter as tk

# root = tk.Tk()

# # Event handler for button click:
# def button_clicked():
#     print("Button Clicked!")

# # Event handler for key press:
# def key_pressed(event):
#     print(f"Key Pressed: {event.char}")

# # Create a Button widget:
# button = tk.Button(root, text="Click Me!", command=button_clicked)

# # Bind key press event to the root window:
# root.bind("<Key>", key_pressed)

# button.pack()

# root.mainloop()


import tkinter as tk

root = tk.Tk()

# Good naming convention
label_hello = tk.Label(root, text="Hello")
button_submit = tk.Button(root, text="Submit")

# Less descriptive naming
lbl = tk.Label(root, text="Hello")
btn = tk.Button(root, text="Submit")

label_hello.pack()
button_submit.pack()

lbl.pack()
btn.pack()

root.mainloop()