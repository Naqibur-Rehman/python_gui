from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("library.sqlite")
cur = con.cursor()


class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x700+550+20')
        self.title("Lend Book")
        self.resizable(False, False)

        query = "SELECT * FROM books WHERE book_status=0"
        books = cur.execute(query).fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0]) + "-" + str(book[1]))

        query2 = "SELECT * FROM members"
        members = cur.execute(query2)
        member_list = []
        for member in members:
            member_list.append(str(member[0]) + "-" + str(member[1]))

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
        heading = Label(self.top_frame, text='   Lend a Book   ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        # ============= Entry and Label =================
        # book combo box
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottom_frame, text='Book : ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.combo_name = ttk.Combobox(self.bottom_frame, textvariable=self.book_name, width=40)
        self.combo_name['values'] = book_list
        self.combo_name.place(x=150, y=45)

        # member combo box
        self.member_name = StringVar()
        self.lbl_member = Label(self.bottom_frame, text='Member : ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_member.place(x=40, y=80)
        self.combo_member = ttk.Combobox(self.bottom_frame, textvariable=self.member_name, width=40)
        self.combo_member['values'] = member_list
        self.combo_member.place(x=150, y=85)

        # Button
        button = Button(self.bottom_frame, text="Lend Book", command=self.lend_book)
        button.place(x=270, y=120)

    def lend_book(self):
        book_name = self.book_name.get()
        member_name = self.member_name.get()
        self.book_id = book_name.split('-')[0]

        if book_name and member_name != "":
            try:
                query = "INSERT INTO 'borrows' (bbook_id, bmember_id) values(?,?) "
                cur.execute(query, (book_name, member_name))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to database!", icon='info')
                cur.execute("UPDATE books SET book_status=? where book_id=?", (1, self.book_id))
                con.commit()
            except:
                messagebox.showerror("Error", "Can't add to database!", icon='warning')
        else:
            messagebox.showerror("Error", "Fields can't be empty!", icon='warning')
