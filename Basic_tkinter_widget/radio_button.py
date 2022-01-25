from tkinter import *
from tkinter import ttk


def callback():
    print("Your name: ", entry.get())
    print("Your name: ", entry2.get())
    if c_var.get() == 1:
        print("Remember me is checked")
    else:
        print("Remember me not checked")
    print(gender.get())


root = Tk()
root.geometry('500x450')

entry = ttk.Entry(root, width=30)
entry.insert(0, "Please enter user name")

entry2 = ttk.Entry(root, width=30)
entry2.insert(0, "Enter password")

button = ttk.Button(root, text="Enter!")

lbl_title = ttk.Label(text="Our Title Here", font=('Arial', 22))
lbl_name = ttk.Label(text="Your Name : ")
lbl_pass = ttk.Label(text="Your Password : ")

lbl_title.grid(row=0, column=0, columnspan=2)
lbl_name.grid(row=1, column=0, sticky='w')
lbl_pass.grid(row=2, column=0, sticky=W, pady=3)        # alternate way

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1, pady=3)

button.grid(row=3, column=1, sticky='ew', pady=5)       # alternate sticky=E+W

c_var = IntVar()
c_var.set(0)
c_box = Checkbutton(root, text="Remember me", variable=c_var, font=("Arial", 16)).grid(row=4, column=0,
                                                                                       sticky='e', columnspan=2)
button.config(command=callback)

gender = StringVar()
ttk.Radiobutton(root, text="Male", value="Male", var=gender).grid(row=5, column=0)
ttk.Radiobutton(root, text="Female", value="Female", var=gender).grid(row=6, column=0)

root.mainloop()
