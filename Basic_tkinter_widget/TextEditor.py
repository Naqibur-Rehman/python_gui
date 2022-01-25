from tkinter import *


def callback():
    result = text_editor.get(1.0, END)
    print(result)


root = Tk()
root.geometry('550x550')

text_editor = Text(root, width=30, height=10, font=('Times', 15), wrap='word')
text_editor.grid(row=0, column=0, padx=20, pady=40)
text_editor.insert(INSERT, "Hello I am a tkinter widget")
text_editor.config(state='disabled')
text_editor.config(state='normal')

button = Button(root, text='Save', width=10, height=1, command=callback).grid(row=1, column=0)

root.mainloop()
