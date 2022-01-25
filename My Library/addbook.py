from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("library.sqlite")
cur = con.cursor()


class Addbook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+20")
        self.title("Add Book")
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
        heading = Label(self.top_frame, text='   Add Book   ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        # ============= Entry and Label =================
        # name
        self.lbl_name = Label(self.bottom_frame, text='Name : ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_name.insert(0, "Please enter a book name")
        self.ent_name.place(x=150, y=45)

        # author name
        self.lbl_author = Label(self.bottom_frame, text='Author : ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_author.place(x=40, y=80)
        self.ent_author = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_author.insert(0, "Please enter author  name")
        self.ent_author.place(x=150, y=85)

        # page
        self.lbl_page = Label(self.bottom_frame, text='Pages : ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_page.place(x=40, y=120)
        self.ent_page = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_page.insert(0, "Please enter number of pages")
        self.ent_page.place(x=150, y=125)

        # language
        self.lbl_language = Label(self.bottom_frame, text='Language : ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_language.place(x=40, y=160)
        self.ent_language = Entry(self.bottom_frame, width=30, bd=4)
        self.ent_language.insert(0, "Please enter language of book")
        self.ent_language.place(x=150, y=165)

        # Button
        button = Button(self.bottom_frame, text="Add Book", command=self.add_book)
        button.place(x=270, y=200)

    def add_book(self):
        name = self.ent_name.get()
        author = self.ent_author.get()
        page = self.ent_page.get()
        language = self.ent_language.get()

        if name and author and page and language != "":
            try:
                query = "INSERT INTO 'books' (book_name, book_author, book_page, book_language) values(?,?,?,?)"
                cur.execute(query, (name, author, page, language))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon="info")
                self.destroy()
            except:
                messagebox.showerror("Error", "Cant add to database", icon='warning')
        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')
