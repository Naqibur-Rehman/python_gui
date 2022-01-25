from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('database.sqlite')
cur = con.cursor()


class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x700+550+10")
        self.title("Add People")
        self.resizable(False, False)
        # ============Frames===========
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=550, bg='#fcc324')
        self.bottom.pack(fill=X)

        # =========== Heading, Image and date==============
        self.top_image = PhotoImage(file='./icons/addperson.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)

        self.heading_lbl = Label(self.top, text="My Person", font='Arial 15 bold',
                                 fg='#003f8a', bg='white')
        self.heading_lbl.place(x=260, y=60)

        # ================================== Label And Entries ========================
        # name
        self.lbl_name = Label(self.bottom, text='Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, "Please Enter Name")
        self.entry_name.place(x=150, y=45)

        # Surname
        self.lbl_surname = Label(self.bottom, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, "Please Enter Surname")
        self.entry_surname.place(x=150, y=85)

        # Email
        self.lbl_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, "Please Enter Email")
        self.entry_email.place(x=150, y=125)

        # Phone
        self.lbl_phone = Label(self.bottom, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, "Please Enter Phone")
        self.entry_phone.place(x=150, y=165)

        # Address
        self.lbl_address = Label(self.bottom, text='Address', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_address.place(x=40, y=300)

        self.entry_address = Text(self.bottom, width=23, height=15, wrap=WORD)
        self.entry_address.place(x=150, y=200)

        # Button
        button = Button(self.bottom, text='Add Person', command=self.add_person)
        button.place(x=270, y=460)


    def add_person(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get(1.0, 'end-1c')

        if name and surname and phone and email and address != "":
            try:
                query = "INSERT INTO 'Persons' (Person_Name, Person_Surname, Person_Email, Person_Phone, " \
                        "Person_Address) Values(?,?,?,?,?)"
                cur.execute(query, (name, surname, email, phone, address))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon='info')
                self.destroy()
            except:
                messagebox.showerror("Failed", "Can't add to database!", icon='warning')
        else:
            messagebox.showerror('Error', "Fields can't be empty!")
