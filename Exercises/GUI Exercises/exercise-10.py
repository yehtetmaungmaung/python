# Write a Python GUI program to create a Listbox bar widgets using
# tkinter module.

import tkinter as tk

root = tk.Tk()
root.geometry('250x200')

label1 = tk.Label(root, text="A list of favorite languages...")

listbox = tk.Listbox(root)
listbox.insert(1, "Go")
listbox.insert(2, "Rust")
listbox.insert(3, "C++")

label1.pack()
listbox.pack()

root.mainloop()