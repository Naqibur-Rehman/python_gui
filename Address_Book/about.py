from tkinter import *


class About:
    def __init__(self, root):
        frame = Frame(root, bg="#ffa500", width=550, height=550)
        frame.pack(fill=BOTH)
        txt = Label(frame, text='''This is our about page you can find
                        \nmore information about us here this application
                        \nwas created for educational purposes only and 
                        \nwe have learned a lot.''',
                    font='arial 15 bold',  bg="#ffa500", fg='white')
        txt.place(x=50, y=50)


def main():
    root = Tk()
    app = About(root)
    root.title("About us")
    root.geometry('550x550+550+10')
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()
