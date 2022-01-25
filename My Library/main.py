import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import addbook
import addmember
import givebook

con = sqlite3.connect("library.sqlite")
cur = con.cursor()


class Main(object):
    def __init__(self, master):
        self.master = master

        def display_statistics(evt):
            count_books = cur.execute("SELECT count(book_id) FROM books").fetchall()
            count_members = cur.execute("SELECT count(member_id) FROM members").fetchall()
            count_taken = cur.execute("SELECT count(book_status) FROM books WHERE book_status=1").fetchall()
            print(count_books)
            self.lbl_book_count.config(text='Total : ' + str(count_books[0][0]) + " Books in Library")
            self.lbl_member_count.config(text='Total members : ' + str(count_members[0][0]))
            self.lbl_taken_count.config(text='Total taken : ' + str(count_taken[0][0]))
            display_books(self)

        def display_books(self):
            books = cur.execute("SELECT * FROM books").fetchall()
            count = 0
            self.list_books.delete(0, END)
            for book in books:
                print(book)
                self.list_books.insert(count, str(book[0]) + "-" + str(book[1]))
                count += 1

            def book_info(evt):
                value = str(self.list_books.get(self.list_books.curselection()))
                id = value.split('-')[0]
                book = cur.execute("SELECT * FROM books WHERE book_id=?", (id,))
                book_info = book.fetchall()
                print(book_info)

                self.list_details.delete(0, 'end')
                self.list_details.insert(0, "Book Name : " + book_info[0][1])
                self.list_details.insert(1, "Author : " + book_info[0][2])
                self.list_details.insert(2, "Page : " + book_info[0][3])
                self.list_details.insert(3, "Language : " + book_info[0][4])

                if book_info[0][5] == 0:
                    self.list_details.insert(4, "Status : Available")
                else:
                    self.list_details.insert(4, "Status : Not Available")

            def double_click(evt):
                global given_id
                value = str(self.list_books.get(self.list_books.curselection()))
                print(value)
                given_id = value.split('-')[0]
                give_book = GiveBook()

            self.list_books.bind("<<ListboxSelect>>", book_info)
            self.tabs.bind("<<NotebookTabChanged>>", display_statistics)
            # self.tabs.bind("<ButtonRelease-1>", display_books)
            # self.list_books.bind("<Double-Button-1>", double_click)

        # ================== Frames =====================
        mainframe = Frame(self.master)
        mainframe.pack()
        # top frame
        top_frame = Frame(mainframe, width=1350, height=70, bg='#f8f8f8', padx=20, relief=SUNKEN, borderwidth=2)
        top_frame.pack(sid=TOP, fill=X)
        # center frame
        center_frame = Frame(mainframe, width=1350, height=680, relief=RIDGE, bg="#e0f0f0")
        center_frame.pack(sid=TOP)
        # center left frame
        center_left_frame = Frame(center_frame, width=900, height=700, bg="#e0f0f0", borderwidth=2, relief="sunken")
        center_left_frame.pack(side='left')
        # center right frame
        center_right_frame = Frame(center_frame, width=450, height=700, bg="#e0f0f0", borderwidth=2, relief="sunken")
        center_right_frame.pack()

        # Search bar
        search_bar = LabelFrame(center_right_frame, width=440, height=175, text='Search Box', bg='#9bc9ff')
        search_bar.pack(fill=BOTH)
        self.lbl_search = Label(search_bar, text='Search : ', font='arial 12 bold', bg='#9bc9ff', fg='white')
        self.lbl_search.grid(row=0, column=0, padx=20, pady=10)
        self.search_entry = Entry(search_bar, width=30, bd=10)
        self.search_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.btn_search = Button(search_bar, text='Search', font='arial 12', bg='#fcc324', fg='white',
                                 command=self.search_book)
        self.btn_search.grid(row=0, column=4, padx=20, pady=10)

        # list bar
        list_bar = LabelFrame(center_right_frame, width=400, height=175, text='List Box', bg='#fcc324')
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar, text='Sort By', font='times 16 bold', fg='#2488ff', bg='#fcc324')
        lbl_list.grid(row=0, column=2)

        self.list_choice = IntVar()
        rb1 = Radiobutton(list_bar, text='All Books', var=self.list_choice, value="1", bg='#fcc324')
        rb2 = Radiobutton(list_bar, text='In Library', var=self.list_choice, value="2", bg='#fcc324')
        rb3 = Radiobutton(list_bar, text='Borrowed Books', var=self.list_choice, value="3", bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)

        btn_list = Button(list_bar, text='List Books', bg='#2488ff', fg='white', font='arial 12', command=self.list_books)
        btn_list.grid(row=1, column=3, padx=40, pady=10)

        # title and image
        image_bar = Frame(center_right_frame, width=440, height=350)
        image_bar.pack(fill=BOTH)
        self.title_right = Label(image_bar, text='Welcome to our Library', font='arial 16 bold')
        self.title_right.grid(row=0)
        self.image_library = PhotoImage(file='./icons/library.png')
        self.lbl_img = Label(image_bar, image=self.image_library)
        self.lbl_img.grid(row=1)

        # ==================================== ToolBar ======================

        # add book
        self.icon_book = PhotoImage(file='./icons/add_book.png')
        self.btn_book = Button(top_frame, text='Add Book', image=self.icon_book, compound=LEFT,
                               font='arial, 12 bold', command=self.add_book)
        self.btn_book.pack(sid=LEFT, padx=10)

        # add member method
        self.icon_member = PhotoImage(file='./icons/users.png')
        self.btn_member = Button(top_frame, text="Add Member", image=self.icon_member, compound="left",
                                 font='arial 12 bold', padx=10, command=self.add_member)
        self.btn_member.pack(side=LEFT)

        # give book
        self.icon_give = PhotoImage(file='./icons/givebook.png')
        self.btn_give = Button(top_frame, text="Give Book", image=self.icon_give, compound="left",
                               font='arial 12 bold', padx=10, command=self.give_book)
        self.btn_give.pack(side='left')

        # ===================== Tabs ==========================
        # ====================== Tab1 ===================
        self.tabs = ttk.Notebook(center_left_frame, width=900, height=660)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file='./icons/books.png')
        self.tab2_icon = PhotoImage(file='./icons/members.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Library Management', image=self.tab1_icon, compound='left')
        self.tabs.add(self.tab2, text='Statistics', image=self.tab2_icon, compound='left')

        # ============== list books ==================
        self.list_books = Listbox(self.tab1, width=40, height=30, bd=5, font='times 12 bold')
        self.scroll = Scrollbar(self.tab1, orient=VERTICAL)
        self.list_books.grid(row=0, column=0, padx=(10, 0), pady=20, sticky=N)
        self.scroll.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=0, sticky=N + S + E)

        # list details'
        self.list_details = Listbox(self.tab1, width=80, height=30, bd=5, font='times 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)

        # ================================ Tab 2 =======================
        # Statistics
        self.lbl_book_count = Label(self.tab2, text="dfsghh", pady=20, font='verdana 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count = Label(self.tab2, text="tye5t", pady=20, font='verdana 14 bold')
        self.lbl_member_count.grid(row=1, sticky=W)
        self.lbl_taken_count = Label(self.tab2, text="ye5yyy", pady=20, font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2, sticky=W)

        # functions
        display_books(self)

        display_statistics(self)

    def add_book(self):
        add = addbook.Addbook()

    def add_member(self):
        member = addmember.Addmember()

    def search_book(self):
        value = self.search_entry.get()
        search = cur.execute("SELECT * FROM books WHERE book_name LIKE ?", ('%' + value + "%",)).fetchall()
        print(search)
        self.list_books.delete(0, 'end')
        count = 0
        for book in search:
            self.list_books.insert(count, str(book[0]) + "-" + str(book[1]))
            count += 1

    def list_books(self):
        value = self.list_choice.get()
        if value == 1:
            all_books = cur.execute("SELECT * FROM books").fetchall()
            self.list_books.delete(0, 'end')

            count = 0
            for book in all_books:
                self.list_books.insert(count, str(book[0]) + "-" + str(book[1]))
                count += 1
        elif value == 2:
            book_in_library = cur.execute("SELECT * FROM books WHERE book_status = ?", (0, )).fetchall()
            self.list_books.delete(0, 'end')

            count = 0
            for book in book_in_library:
                self.list_books.insert(count, str(book[0]) + "-" + str(book[1]))
                count += 1
        else:
            taken_book = cur.execute("SELECT * FROM books WHERE book_status = ?", (1, )).fetchall()
            self.list_books.delete(0, 'end')

            count = 0
            for book in taken_book:
                self.list_books.insert(count, str(book[0]) + "-" + str(book[1]))
                count += 1

    def give_book(self):
        give_book = givebook.GiveBook()


class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x700+550+20')
        self.title("Lend Book")
        self.resizable(False, False)
        global given_id
        self.book_id = int (given_id)

        query = "SELECT * FROM books "
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
        self.combo_name.current(self.book_id-1)
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


def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1350x750")
    root.iconbitmap('./icons/icon.ico')
    root.mainloop()


if __name__ == "__main__":
    main()
