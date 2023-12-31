# Write a Python GUI program to create a Spinbox widget using tkinter module.

import tkinter as tk
root = tk.Tk()

text_var = tk.DoubleVar()

spin_box = tk.Spinbox(
    root,
    from_=0.6,
    to=500.0,
    increment=.01,
    textvariable=text_var,
)

spin_box.pack()
root.mainloop()