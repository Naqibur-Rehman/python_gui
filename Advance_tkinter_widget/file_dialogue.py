from tkinter import *
from tkinter import filedialog, colorchooser


def open_file():
    file_name = filedialog.askopenfilename(initialdir='./', title="Select a file",
                                           filetypes=(("Txt files", ".txt"), ("All Files", "*.*")))
    content = open(file_name).read()
    text_editor.insert(END, content)


def save_file():
    my_file = filedialog.asksaveasfile(initialdir='./', mode="w", defaultextension='.txt')
    if my_file is None:
        return
    content = text_editor.get(1.0, 'end-1c')
    my_file.write(content)


def change_color():
    color = colorchooser.askcolor()
    print(color)
    text_editor.config(fg=color[1])


root = Tk()
root.geometry('450x350+750+100')
root.title("File Dialogue")

text_editor = Text(root, width=25, height=15, wrap='word')
text_editor.pack()

button = Button(root, text='Open', command=open_file).pack(side=LEFT, padx=(150, 20))
button2 = Button(root, text='Save', command=save_file).pack(side=LEFT)
button3 = Button(root, text='Color', command=change_color).pack(side=LEFT, padx=20)

root.mainloop()
