from tkinter import *
import datetime
import mypeople, about


date = datetime.date.today()


class Application():
    def __init__(self, master):
        self.master = master

        # ============Frames===========
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=400, bg='#adff2f')
        self.bottom.pack(fill=X)

        # =========== Heading, Image and date==============
        self.top_image = PhotoImage(file='./icons/book.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)

        self.heading_lbl = Label(self.top, text="My Address Book", font='Arial 15 bold',
                                 fg='#ffa500', bg='white')
        self.heading_lbl.place(x=260, y=60)

        self.date_label = Label(self.top, text="Today's Date : " + str(date), font='arial 12 bold',
                                fg='#ffa500', bg='white')
        self.date_label.place(x=450, y=5)

        # ================== Button 1 ===============
        self.btn1_icon = PhotoImage(file='./icons/man.png')
        self.person_btn = Button(self.bottom, text='   My People   ', font='arial 12 bold',
                                 command=self.my_people)
        self.person_btn.config(image=self.btn1_icon, compound=LEFT)
        self.person_btn.place(x=250, y=10)

        # ================== Button 2 ===============
        self.btn2_icon = PhotoImage(file='./icons/add.png')
        self.add_btn = Button(self.bottom, text='  Add People  ', font='arial 12 bold', command=self.funcaddpeople)
        self.add_btn.config(image=self.btn2_icon, compound=LEFT)
        self.add_btn.place(x=250, y=70)

        # ================== Button 3 ===============
        self.btn3_icon = PhotoImage(file='./icons/info.png')
        self.info_btn = Button(self.bottom, text='    About Us    ', font='arial 12 bold', command=about.main)
        self.info_btn.config(image=self.btn3_icon, compound=LEFT)
        self.info_btn.place(x=250, y=130)

    def my_people(self):
        people = mypeople.MyPeople()

    def funcaddpeople(self):
        people = mypeople.addpeople.AddPeople()


def main():
    root = Tk()
    app = Application(root)
    root.title("Address Book")
    root.geometry('650x550+350+100')
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
