from tkinter import *

root = Tk()
root.geometry('320x250')
label = Label(root, text="Hello Python")
# label['text'] = "Hello Tkinter"
label.config(text="Hello Tkinter", fg="red")
label.config(bg="cyan")
label.config(text="Hello Python I love you so much")
label.config(wraplength="150")
label.config(justify="right")
label.config(font="Times 15")
label.pack()

root.mainloop()
