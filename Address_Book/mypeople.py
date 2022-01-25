from tkinter import *
from tkinter import messagebox
import sqlite3
import addpeople


con = sqlite3.connect('database.sqlite')
cur = con.cursor()


class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+620+20')
        self.title("My People")
        self.resizable(False, False)

        # ============Frames===========
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg='#fcc324')
        self.bottom.pack(fill=X)

        # =========== Heading, Image and date==============
        self.top_image = PhotoImage(file='./icons/person_icon.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)

        self.heading = Label(self.top, text="My Person", font='Arial 15 bold',
                             fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        # ===================== Scrollbar ====================
        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        # ================ listBox ========================
        self.listbox = Listbox(self.bottom, width=60, height=31)
        self.listbox.grid(row=0, column=0, padx=(14, 0))
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky=N+S)

        persons = cur.execute("SELECT * FROM Persons").fetchall()
        print(persons)
        count = 0
        for person in persons:
            self.listbox.insert(count, str(person[0]) + "-" + person[1] + " " + person[2])
            count += 1

        # Button
        btn_add = Button(self.bottom, text="Add", width=12, font='sans 12 bold', command=self.add_people)
        btn_add.grid(row=0, column=2, sticky=N, padx=5, pady=10)

        btn_update = Button(self.bottom, text="Update", width=12, font='sans 12 bold', command=self.update_people)
        btn_update.grid(row=0, column=2, sticky=N, padx=5, pady=50)

        btn_display = Button(self.bottom, text="Display", width=12, font='sans 12 bold', command=self.display)
        btn_display.grid(row=0, column=2, sticky=N, padx=5, pady=90)

        btn_delete = Button(self.bottom, text="Delete", width=12, font='sans 12 bold', command=self.delete)
        btn_delete.grid(row=0, column=2, sticky=N, padx=5, pady=130)

    def add_people(self):
        add_page = addpeople.AddPeople()
        self.destroy()

    def update_people(self):
        global person_id
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split('-')[0]

        update_page = Update()
        self.destroy()

    def display(self):
        global person_id
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split('-')[0]
        display_page = Display()
        self.destroy()

    def delete(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split('-')[0]

        mbox = messagebox.askquestion("Warning", "Are you sure ?", icon='warning')
        if mbox == 'yes':
            try:
                cur.execute("DELETE FROM Persons WHERE Person_Id=?", (person_id,))
                con.commit()
                messagebox.showinfo("Success", "Person has been deleted!")
                self.destroy()
            except:
                messagebox.showinfo("Info", "Person has not been deleted!")


class Update(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+550+20")
        self.title("Update Person")
        self.resizable(False, False)

        # get person from database
        global person_id

        person = cur.execute("SELECT * FROM Persons WHERE Person_Id = ?", (person_id,))
        person_info = person.fetchall()
        print(person_info)
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]

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
        self.entry_name.insert(0, self.person_name)
        self.entry_name.place(x=150, y=45)

        # Surname
        self.lbl_surname = Label(self.bottom, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, self.person_surname)
        self.entry_surname.place(x=150, y=85)

        # Email
        self.lbl_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, self.person_email)
        self.entry_email.place(x=150, y=125)

        # Phone
        self.lbl_phone = Label(self.bottom, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, self.person_phone)
        self.entry_phone.place(x=150, y=165)

        # Address
        self.lbl_address = Label(self.bottom, text='Address', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_address.place(x=40, y=300)

        self.entry_address = Text(self.bottom, width=23, height=15, wrap=WORD)
        self.entry_address.place(x=150, y=200)
        self.entry_address.insert('1.0', self.person_address)

        # Button
        button = Button(self.bottom, text='Update Person', command=self.update_person)
        button.place(x=270, y=460)

    def update_person(self):
        person_id = self.person_id
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get(1.0, 'end-1c')

        try:
            query = "UPDATE Persons set Person_Name=?, Person_Surname=?, Person_Email=?, Person_Phone=?," \
                    " Person_Address=? WHERE Person_Id=?"
            cur.execute(query, (name, surname, email, phone, address, person_id))
            con.commit()
            messagebox.showinfo("Success", "Successfully has been updated!", icon='info')
            self.destroy()
        except:
            messagebox.showerror("Warning", "Person has not been updated!", icon='warning')


class Display(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+550+20")
        self.title("Display Person")
        self.resizable(False, False)

        # get person from database
        global person_id

        person = cur.execute("SELECT * FROM Persons WHERE Person_Id = ?", (person_id,))
        person_info = person.fetchall()
        print(person_info)
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]

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
        self.entry_name.insert(0, self.person_name)
        self.entry_name.config(state='disabled')
        self.entry_name.place(x=150, y=45)

        # Surname
        self.lbl_surname = Label(self.bottom, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, self.person_surname)
        self.entry_surname.config(state='disabled')
        self.entry_surname.place(x=150, y=85)

        # Email
        self.lbl_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, self.person_email)
        self.entry_email.config(state='disabled')
        self.entry_email.place(x=150, y=125)

        # Phone
        self.lbl_phone = Label(self.bottom, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, self.person_phone)
        self.entry_phone.config(state='disabled')
        self.entry_phone.place(x=150, y=165)

        # Address
        self.lbl_address = Label(self.bottom, text='Address', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_address.place(x=40, y=300)

        self.entry_address = Text(self.bottom, width=23, height=15, wrap=WORD)
        self.entry_address.place(x=150, y=200)
        self.entry_address.insert('1.0', self.person_address)
        self.entry_address.config(state='disabled')
