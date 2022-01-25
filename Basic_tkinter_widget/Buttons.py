from tkinter import *

root = Tk()
root.geometry("350x300")


def callback():
    label.config(text="You Clicked Me!!", fg="red", bg="yellow")


label = Label(root, text="Hello Python")
label.pack()

button = Button(root, text="Click Me!", command=callback)
button.pack()
button['state'] = 'disabled'
button['state'] = 'normal'

root.mainloop()
