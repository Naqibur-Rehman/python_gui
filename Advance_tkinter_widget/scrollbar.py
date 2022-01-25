from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('500x450')
root.title("ScrollBar")

text_box = Text(root, width=60, height=20, wrap='word')
text_box.grid(row=0, column=0)

scroll = Scrollbar(root, orient=VERTICAL, command=text_box.yview)
scroll.grid(row=0, column=1, sticky=N+S)

text_box.config(yscrollcommand=scroll.set)

root.mainloop()
