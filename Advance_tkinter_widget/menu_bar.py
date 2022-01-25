from tkinter import *
from tkinter import messagebox


def func1():
    mbox = messagebox.askquestion("Exit", "Are you sure", icon="warning")
    if mbox == 'yes':
        root.destroy()


root = Tk()
root.geometry('650x650+700+100')
root.title("Menu")

menu_bar = Menu(root)
root.config(menu=menu_bar)
file = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file)
file.add_command(label='New')
file.add_separator()
file.add_command(label='Open')
file.add_command(label='Save')
icon = PhotoImage(file='icons/off.png')
file.add_command(label='Exit', image=icon, compound=LEFT, command=func1)

edit = Menu(menu_bar)
menu_bar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Copy")
edit.add_command(label="Paste")

about = Menu(menu_bar)


root.mainloop()