from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("library.sqlite")
cur = con.cursor()


class Addmember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+20")
        self.title("Add Member")
        self.resizable(False, False)

        # ============= Frames ==================

        # Top Frame
        self.top_frame = Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=X)

        # Bottom Frame
        self.bottom_frame = Frame(self, height=600, bg='#fcc324')
        self.bottom_frame.pack(fill=X)

        # heading, image
        self.top_image = PhotoImage(file='./icons/addbook.png')
        top_image_lbl = Label(self.top_frame, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.top_frame, text='   Add Member   ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        # ============= Entry and Label =================
        # member name
        self.lbl_name = Label(self.bottom_frame, text='Name : ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_name.insert(0, "Please enter a member name")
        self.ent_name.place(x=150, y=45)

        # phone
        self.lbl_phone = Label(self.bottom_frame, text='Phone : ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=80)
        self.ent_phone = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_phone.insert(0, "Please enter phone number")
        self.ent_phone.place(x=150, y=85)

        # Button
        button = Button(self.bottom_frame, text="Add Member", command=self.add_member)
        button.place(x=270, y=120)

    def add_member(self):
        name = self.ent_name.get()
        phone = self.ent_phone.get()

        if name and phone != "":
            try:
                query = "INSERT INTO 'members' (member_name, member_phone) values(?,?)"
                cur.execute(query, (name, phone))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon="info")
                self.destroy()
            except:
                messagebox.showerror("Error", "Cant add to database", icon='warning')
        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')
