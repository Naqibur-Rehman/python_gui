from tkinter import *
from tkinter import ttk


def callback():
    val1 = entry.get()
    val2 = entry2.get()
    print("Your name is: ", val1)
    print("Your password is: ", val2)


root = Tk()
root.geometry('300x300')

entry = ttk.Entry(root, width=30)
entry.pack()
entry.insert(0, "please enter user name")
entry2 = Entry(root, width=30)
entry2.pack()
entry2.config(show="*")

entry.state(['disabled'])
entry.state(['!disabled'])
entry.state(['readonly'])

button = ttk.Button(root, text="Click Me!", command=callback)
button.pack()

root.mainloop()
