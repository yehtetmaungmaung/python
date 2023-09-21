# Write a Python GUI program to create two buttons exit and hello using
#tkinter module.On pressing hello button print the text “Tkinter is 
# easy to create GUI” on the terminal.

import tkinter as tk

def print_hello():
    print("Tkinter is easy to create GUI")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

hello_button = tk.Button(
    frame,
    text="hello",
    command=print_hello
)
hello_button.pack(side=tk.LEFT)

exit_button = tk.Button(
    frame,
    text="exit",
    fg="green",
    command=quit
)
exit_button.pack(side=tk.RIGHT)

root.mainloop()