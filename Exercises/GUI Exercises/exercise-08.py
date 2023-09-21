# Write a Python GUI program to create a ScrolledText widgets using tkinter module.

import tkinter as tk
import tkinter.scrolledtext as tkst

root = tk.Tk()

root.title("ScrolledText")
root.geometry('350x200')

txt = tkst.ScrolledText(
    root,
    width=40,
    height=10
)
txt.grid(column=0, row=0)

root.mainloop()