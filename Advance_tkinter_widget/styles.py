from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk


root = tk.ThemedTk()
root.get_themes()
root.set_theme('breeze')
root.geometry('400x550+750+100')
root.title("Style")

text_name = ttk.Label(root, text='Name: ').grid(row=0, column=0, pady=20)
sur_name = ttk.Label(root, text='SurName: ').grid(row=1, column=0)
txt_msg = ttk.Label(root, text="Message: ")
name_input = ttk.Entry(root, width=30)
sur_name_input = ttk.Entry(root, width=30)
name_input.insert(0, "Please enter your name")
sur_name_input.insert(0, "Please enter your surname")
name_input.grid(row=0, column=1)
sur_name_input.grid(row=1, column=1)
ttk.Radiobutton(root, text='male', value='Male').grid(row=2, column=1, sticky=E, pady=15)
ttk.Radiobutton(root, text='female', value='Female').grid(row=2, column=2)
msg_txt = Text(root, width=25, height=15, wrap='word').grid(row=3, column=1)
button1 = ttk.Button(root, text='Send', width=10).grid(row=4, column=1, sticky=W)
button2 = ttk.Button(root, text='Clear', width=10).grid(row=4, column=1, sticky=E)


root.mainloop()
