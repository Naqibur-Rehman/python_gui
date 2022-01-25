from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('650x650+700+100')
root.title("Tabs")

icon = PhotoImage(file='icons/add.png')

tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH, expand=TRUE)

tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)

tabs.add(tab1, text="Tab_1")
tabs.add(tab2, text="Tab_2", image=icon, compound=LEFT)

label = Label(tab1, text="Hello").place(x=200, y=200)

button = ttk.Button(tab2, text="Click Me!").place(x=250, y=50)

root.mainloop()
