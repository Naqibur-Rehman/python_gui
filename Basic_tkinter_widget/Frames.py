from tkinter import *

root = Tk()
root.geometry('650x650')
root.title("Frames")

frame = Frame(root, height=300, width=300, bg='cyan', bd='5', relief='sunken')
frame.pack(fill=X)

button1 = Button(frame, text='Button1').pack(side=LEFT, padx=20, pady=50)
button2 = Button(frame, text='Button2').pack(side="left", padx=20, pady=50)

search_bar = LabelFrame(root, text='Search Box', padx=20, pady=20, bg='turquoise')
search_bar.pack(side='top')
lbl = Label(search_bar, text="Search")
lbl.pack(side='left', padx=10)
entry = Entry(search_bar)
entry.pack(side=LEFT, padx=10)
button = Button(search_bar, text="Search")
button.pack(side=LEFT, padx=10)

root.mainloop()
