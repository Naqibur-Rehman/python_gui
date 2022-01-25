from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('650x650+700+100')
root.title("Using_Image")

lbl_text = Label(root, text="Using Images", font=("Times", 15))
lbl_text.pack()

logo = PhotoImage(file='icons/add.png')

lbl_image = Label(root, image=logo)
lbl_image.pack()

root.mainloop()
