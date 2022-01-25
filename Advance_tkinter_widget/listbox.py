from tkinter import *
from tkinter import ttk


def print_me():
    selected = listbox.curselection()
    for item in selected:
        print(listbox.get(item))


def delete_me():
    selected = listbox.curselection()
    for item in selected:
        listbox.delete(item)


root = Tk()
root.geometry('650x650+700+100')
root.title("ListBox")

listbox = Listbox(root, width=40, height=15, selectmode=MULTIPLE)
listbox.pack(pady=20)
listbox.insert(0, "Python")
listbox.insert(1, "C++")
listbox.insert(2, "C")
listbox.insert(3, "PHP")

button = ttk.Button(root, text="Print", command=print_me).place(x=300, y=350)
button1 = Button(root, text="Delete", command=delete_me).place(x=350, y=350)

root.mainloop()
