# To test Checkbox

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

my_bool_var = tk.BooleanVar()

my_checkbutton = ttk.Checkbutton(
    text="Check when the option is True.",
    variable=my_bool_var
)

my_checkbutton.pack()
root.mainloop()