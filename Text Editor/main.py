from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox

showStatusBar = True
showToolBar = True
fontFamily = "Arial"
url = ""
fontSize = 12
text_changed = False


class FindDialog(Toplevel):
    def __init__(self, parent, *args, **kwargs):
        Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.geometry("450x200+550+200")
        self.title("Find")
        self.resizable(False, False)

        txt_find = Label(self, text="Find : ")
        txt_find.place(x=20, y=20)

        txt_replace = Label(self, text="Replace : ")
        txt_replace.place(x=20, y=60)

        self.find_input = Entry(self, width=30, )
        self.find_input.place(x=100, y=20)
        self.replace_input = Entry(self, width=30, )
        self.replace_input.place(x=100, y=60)

        self.btn_find = Button(self, text="Find", command=self.parent.find_words)
        self.btn_replace = Button(self, text="Replace", command=self.parent.replace_words)
        self.btn_find.place(x=200, y=90)
        self.btn_replace.place(x=240, y=90)


class MainMenu(Menu):
    def __init__(self, parent, *args, **kwargs):
        Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # ================= File Menu ===============
        self.new_icon = PhotoImage(file='./icons/new.png')
        self.open_icon = PhotoImage(file='./icons/open.png')
        self.save_icon = PhotoImage(file='./icons/save_icon.png')
        self.exit_icon = PhotoImage(file='./icons/exit.png')

        self.file = Menu(self, tearoff=0)
        self.file.add_command(label=' New', image=self.new_icon, compound='left', accelerator="Ctrl+N",
                              command=self.parent.new_file)
        self.file.add_command(label=" Open", accelerator="Ctrl+O", image=self.open_icon, compound='left',
                              command=self.parent.open_file)
        self.file.add_command(label=" Save", accelerator="Ctrl+S", image=self.save_icon, compound='left',
                              command=self.parent.save_file)
        self.file.add_command(label=" Save As", accelerator="Ctrl+Alt+S", compound='left',
                              command=self.parent.save_as_file)
        self.file.add_command(label=" Exit", image=self.exit_icon, compound='left',
                              command=self.parent.exit_func)

        # ==================== Edit Menu ========================
        self.edit = Menu(self, tearoff=0)
        self.edit.add_command(label='Copy', accelerator="Ctrl+C",
                              command=lambda: self.parent.text_editor.event_generate("<Control c>"))
        self.edit.add_command(label='Paste', accelerator="Ctrl+V",
                              command=lambda: self.parent.text_editor.event_generate("<Control v>"))
        self.edit.add_command(label='Cut', accelerator="Ctrl+X",
                              command=lambda: self.parent.text_editor.event_generate("<Control x>"))
        self.edit.add_command(label='Clear All', accelerator="Ctrl+Alt+C",
                              command=lambda: self.parent.text_editor.delete(1.0, 'end'))
        self.edit.add_command(label='Find', accelerator="Ctrl+F", command=self.parent.find)

        # ===================== View Menu =====================
        global showStatusBar
        global showToolBar
        self.view = Menu(self, tearoff=0)
        self.view.add_checkbutton(onvalue=True, offvalue=False, label="Tool Bar", variable=showToolBar,
                                  command=self.parent.hide_toolbar)
        self.view.add_checkbutton(onvalue=True, offvalue=False, label="Status Bar", variable=showStatusBar,
                                  command=self.parent.hide_statusbar)

        # =========================== Themes Menu =============================
        self.themes = Menu(self, tearoff=0)
        self.color_list = {
            'Default': '#000000.#FFFFFF',  # first one is font color second one is background
            'Tomato': '#ffff00.#ff6347',
            'Lime Green': '#fffff0.#32cd32',
            'Magenta': '#fffafa.#ff00ff',
            'Royal Blue': '#ffffbb.#4169e1',
            'Medium Blue': '#d1e7e0.#0000cd',
            'Dracula': '#ffffff.#000000'
        }
        self.theme_choice = StringVar()
        for i in sorted(self.color_list):
            self.themes.add_radiobutton(label=i, variable=self.theme_choice, command=self.change_theme)

        self.add_cascade(label='File', menu=self.file)
        self.add_cascade(label='Edit', menu=self.edit)
        self.add_cascade(label='View', menu=self.view)
        self.add_cascade(label='Theme', menu=self.themes)
        self.about = Menu(self, tearoff=0)
        self.add_cascade(label='About', command=self.parent.about_us)

    def change_theme(self):
        selected_theme = self.theme_choice.get()
        fg_bg_color = self.color_list.get(selected_theme)
        print(fg_bg_color)
        fg, bg = fg_bg_color.split('.')
        self.parent.text_editor.config(background=bg, fg=fg)


class TextEditor(Text):
    def __init__(self, parent, *args, **kwargs):
        Text.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(wrap='word')
        self.pack(fill="both", expand='yes')  # expand=True/YES/'true'/'yes'
        self.config(relief=FLAT)
        # x_scrollbar = Scrollbar(self, orient=HORIZONTAL)
        # x_scrollbar.pack(side=BOTTOM, fill=X)
        # x_scrollbar.config(command=self.xview)
        # y_scrollbar = Scrollbar(self, orient='vertical')
        # y_scrollbar.pack(side='right', fill='y')
        # y_scrollbar.config(command=self.yview)

        scroll_bar = Scrollbar(self, bd=5, relief=SUNKEN)
        self.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.yview)
        scroll_bar.pack(side=RIGHT, fill=Y)


class StatusBar(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(side='bottom')
        self.config(text='Status Bar')


class ToolBar(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(side=TOP, fill=X)

        # combobox
        self.cb_font = ttk.Combobox(self)
        self.cb_font_size = ttk.Combobox(self)
        self.cb_font.pack(sid='left', padx=(5, 10))
        self.cb_font_size.pack(sid='left')

        # =================Bold Button ======================
        self.bold_icon = PhotoImage(file='./icons/bold.png')
        btn_bold = Button(self, image=self.bold_icon, command=self.parent.change_bold)
        btn_bold.pack(side=LEFT, padx=5)

        # =================Italic Button ======================
        self.italic_icon = PhotoImage(file='./icons/italic.png')
        btn_italic = Button(self, image=self.italic_icon, command=self.parent.change_italic)
        btn_italic.pack(side=LEFT, padx=5)

        # =================Underline Button ======================
        self.underline_icon = PhotoImage(file='./icons/under_line.png')
        btn_underline = Button(self, image=self.underline_icon, command=self.parent.change_underline)
        btn_underline.pack(side=LEFT, padx=5)

        # =================Font color Button ======================
        self.font_color_icon = PhotoImage(file='./icons/color.png')
        btn_font_color = Button(self, image=self.font_color_icon, command=self.parent.change_color)
        btn_font_color.pack(side=LEFT, padx=5)

        # =================Align Left Button ======================
        self.align_left_icon = PhotoImage(file='./icons/alignleft.png')
        btn_align_left = Button(self, image=self.align_left_icon, command=self.parent.change_align_left)
        btn_align_left.pack(side=LEFT, padx=5)

        # =================Align Center Button ======================
        self.align_center_icon = PhotoImage(file='./icons/aligncenter.png')
        btn_center_left = Button(self, image=self.align_center_icon, command=self.parent.change_align_center)
        btn_center_left.pack(side=LEFT, padx=5)

        # =================Align Right Button ======================
        self.align_right_icon = PhotoImage(file='./icons/alignright.png')
        btn_align_right = Button(self, image=self.align_right_icon, command=self.parent.change_align_right)
        btn_align_right.pack(side=LEFT, padx=5)

        # ============= Font Family ======================
        fonts = font.families()
        fonts_list = []
        fonts_size_list = []

        for i in range(8, 80):
            fonts_size_list.append(i)

        for i in fonts:
            fonts_list.append(i)

        self.font_var = StringVar()
        self.cb_font.config(values=fonts_list, textvariable=self.font_var)
        self.cb_font.current(0)
        self.cb_font_size.config(values=fonts_size_list)
        self.cb_font_size.current(4)

        self.cb_font.bind("<<ComboboxSelected>>", self.parent.get_font)
        self.cb_font_size.bind("<<ComboboxSelected>>", self.parent.get_font_size)


class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(fill=BOTH, expand=True)

        # ============= Creating widget ================
        self.main_menu = MainMenu(self)
        self.tool_bar = ToolBar(self)
        self.text_editor = TextEditor(self)
        self.status_bar = StatusBar(self)

        # Parent menu configuration
        self.parent.config(menu=self.main_menu)

        # setting focus
        self.text_editor.focus()
        self.text_editor.configure(font=('arial', 12))
        self.text_editor.bind('<<Modified>>', self.changed)

    def about_us(self, *args):
        messagebox.showinfo("About", "This is our about page\nhave a question\ncontact us at dev@gmail.com")

    def exit_func(self, *args):
        global url
        global text_changed
        try:
            if text_changed is True:
                m_box = messagebox.askyesnocancel("Warning", "Do you want to save the file?")
                if m_box is True:
                    if url != "":
                        content = self.text_editor.get(1.0, 'end')
                        with open(url, 'w', encoding='utf-8') as file:
                            file.write(content)
                            self.parent.destroy()
                    else:
                        content2 = str(self.text_editor.get(1.0, 'end'))
                        url = filedialog.asksaveasfile(mode="w", defaultextension=".txt",
                                                       filetypes=(("Text files", "*.txt"), ("All files", "*-*")))
                        url.write(content2)
                        url.close()
                if m_box is False:
                    self.parent.destroy()
            else:
                self.parent.destroy()
        finally:
            return

    def save_as_file(self, *args):
        global url
        try:
            url = filedialog.asksaveasfile(initialdir="./", mode="w", defaultextension=".txt",
                                           filetypes=(("Text files", "*.txt"), ("All files", "*-*")))
            content = str(self.text_editor.get(1.0, 'end'))
            url.write(content)
            url.close()
            self.parent.title("Text Editor - Now Editing " + str(url.split('/')[-1]))
        finally:
            return

    def save_file(self, *args):
        global url
        try:
            if url != "":
                content = str(self.text_editor.get(1.0, END))
                print(content)
                with open(url, 'w', encoding='utf-8') as file:
                    file.write(content)
            else:
                url = filedialog.asksaveasfile(initialdir='./', mode='w', defaultextension=".txt",
                                               filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
                content2 = str(self.text_editor.get(1.0, END))
                print(content2)
                url.write(content2)
                print(url)
                url.close()
        finally:
            return

    def open_file(self, *args):
        global url
        url = filedialog.askopenfilename(initialdir='./', title='Select a file to open',
                                         filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        try:
            with open(url, 'r') as file:
                self.text_editor.delete(1.0, END)
                self.text_editor.insert(1.0, file.read())
        finally:
            self.parent.title("Text Editor - Now Editing " + str(url.split('/')[-1]))
            print(url.split('/'))

    def new_file(self, *args):
        global url
        try:
            url = ""
            self.text_editor.delete(1.0, 'end')
        finally:
            pass

    def changed(self, *args):
        global text_changed
        flag = self.text_editor.edit_modified()
        text_changed = True
        print(flag)
        if flag:
            words = len(self.text_editor.get(1.0, 'end-1c').split())
            letters = len(self.text_editor.get(1.0, 'end-1c'))
            self.status_bar.config(text='Characters: ' + str(letters) + " Words: " + str(words))

        self.text_editor.edit_modified(False)

    def get_font(self, *args):
        global fontFamily
        fontFamily = self.tool_bar.cb_font.get()
        print(fontFamily)
        self.text_editor.config(font=(fontFamily, fontSize))

    def get_font_size(self, *args):
        global fontSize
        fontSize = self.tool_bar.cb_font_size.get()
        self.text_editor.config(font=(fontFamily, fontSize))

    def change_bold(self, *args):
        text_pro = font.Font(font=self.text_editor['font'])
        print(text_pro.actual('weight'))

        if text_pro.actual('weight') == "normal":
            self.text_editor.configure(font=(fontFamily, fontSize, 'bold'))
        elif text_pro.actual('weight') == "bold":
            self.text_editor.configure(font=(fontFamily, fontSize, 'normal'))

    def change_italic(self, *args):
        text_pro = font.Font(font=self.text_editor['font'])
        print(text_pro.actual())

        if text_pro.actual('slant') == "roman":
            self.text_editor.configure(font=(fontFamily, fontSize, 'italic'))
        elif text_pro.actual('slant') == "italic":
            self.text_editor.configure(font=(fontFamily, fontSize, 'roman'))

    def change_underline(self, *args):
        text_pro = font.Font(font=self.text_editor['font'])
        print(text_pro.actual())

        if text_pro.actual('underline') == 0:
            self.text_editor.configure(font=(fontFamily, fontSize, 'underline'))
        elif text_pro.actual('underline') == 1:
            self.text_editor.configure(font=(fontFamily, fontSize, 'normal'))

    def change_color(self, *args):
        color = colorchooser.askcolor()
        print(color)
        self.text_editor.configure(fg=color[1])

    def change_align_left(self, *args):
        content = self.text_editor.get(1.0, 'end')
        self.text_editor.tag_config('left', justify=LEFT)
        self.text_editor.delete(1.0, 'end')
        self.text_editor.insert(INSERT, content, 'left')

    def change_align_center(self, *args):
        content = self.text_editor.get(1.0, 'end')
        self.text_editor.tag_config('center', justify=CENTER)
        self.text_editor.delete(1.0, 'end')
        self.text_editor.insert(INSERT, content, 'center')

    def change_align_right(self, *args):
        content = self.text_editor.get(1.0, 'end')
        self.text_editor.tag_config('right', justify=RIGHT)
        self.text_editor.delete(1.0, 'end')
        self.text_editor.insert(INSERT, content, 'right')

    def find(self, *args):
        self.find = FindDialog(parent=self)

    def find_words(self, *args):
        word = self.find.find_input.get()
        print(word)
        self.text_editor.tag_remove('match', '1.0', 'end')
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = self.text_editor.search(word, start_pos, stopindex='end')
                if not start_pos:
                    break
                end_pos = '{}+{}c'.format(start_pos, len(word))
                self.text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                self.text_editor.tag_config('match', foreground='red', background='yellow')

    def replace_words(self, *args):
        replace_txt = self.find.replace_input.get()
        word = self.find.find_input.get()
        content = self.text_editor.get(1.0, 'end')
        new_value = content.replace(word, replace_txt)
        self.text_editor.delete(1.0, END)
        self.text_editor.insert(1.0, new_value)

    def hide_statusbar(self, *args):
        global showStatusBar
        if showStatusBar:
            self.status_bar.pack_forget()
            showStatusBar = False
        else:
            self.status_bar.pack()
            showStatusBar = True

    def hide_toolbar(self, *args):
        global showToolBar
        if showToolBar:
            self.tool_bar.pack_forget()
            showToolBar = False
        else:
            self.text_editor.pack_forget()
            self.status_bar.pack_forget()
            self.tool_bar.pack(side="top", fill=X)
            self.text_editor.pack(expand=YES, fill=BOTH)
            self.status_bar.pack(sid=BOTTOM)
            showToolBar = True


if __name__ == '__main__':
    root = Tk()
    root.title("Text Editor")
    MainApplication(root).pack(side='top', fill=BOTH, expand=True)
    root.iconbitmap('./icons/icon.ico')
    root.geometry('1250x650+50+25')
    root.mainloop()
