# Write a Python GUI program to add a canvas in your application using tkinter module.

import tkinter as tk

root = tk.Tk()

canvas_width = 100
canvas_height = 80
w = tk.Canvas(
    root,
    width=canvas_width,
    height=canvas_height
)
w.pack()

y = int(canvas_height/2)
w.create_line(0, y, canvas_width, y, fill="#476042")

root.mainloop()