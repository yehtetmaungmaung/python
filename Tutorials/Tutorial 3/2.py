from tkinter import *

root = Tk()
menu = Menu(root, tearoff=0)
menubar = Menu(menu, tearoff=0)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as")
filemenu.add_command(label="Print")
filemenu.add_command(label="Close")
filemenu.add_command(label="Exit")
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
menubar.add_cascade(label="Edit", menu=editmenu)
root.config(menu=menubar)
root.mainloop()