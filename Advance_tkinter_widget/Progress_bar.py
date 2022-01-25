from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('450x450+750+150')

pro_bar = ttk.Progressbar(root, orient='horizontal', length=200)        # orient=HORIZONTAL
pro_bar.pack(pady=20)
pro_bar.config(mode='indeterminate')
pro_bar.start()
pro_bar.stop()
pro_bar.config(mode='determinate', maximum=50.0, value=10.0)
pro_bar.start()
pro_bar.stop()

value = DoubleVar()
pro_bar.config(variable=value)
scale = ttk.Scale(root, orient=HORIZONTAL, length=200, var=value, from_=0.0, to=50.0)
scale.pack()

root.mainloop()
