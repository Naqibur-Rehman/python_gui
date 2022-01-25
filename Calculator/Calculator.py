from tkinter import *


def enter_number(x):
    if entry_box.get() == 'O':
        entry_box.delete(0, 'end')
        entry_box.insert(0, str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length, str(x))


def enter_operator(x):
    if entry_box.get() != "O":
        length = len(entry_box.get())
        entry_box.insert(length, btn_operator[x]['text'])


def clear_number():
    entry_box.delete(0, END)
    entry_box.insert(0, "O")


result_list = []


def equal_operator():
    content = entry_box.get()
    print(content)
    print(type(content))
    result = eval(content)
    print(result)
    entry_box.delete(0, 'end')
    entry_box.insert(0, str(result))

    result_list.append(content)
    result_list.reverse()
    status_bar.configure(text="History : " + '|' .join(result_list[:5]), font='verdana 10 bold')


def delete_operator():
    length = len(entry_box.get())
    entry_box.delete(length-1, 'end')
    if length == 1:
        entry_box.insert(0, "O")


root = Tk()
root.geometry("380x550+750+100")
root.title("Calculator")
root.resizable(False, False)

# ========================= EntryBox ========================
entry_box = Entry(root, font='verdana 14 bold', width=22, bd=10, justify="right", bg='#e6e6fa')
entry_box.place(x=20, y=10)
entry_box.insert(0, "O")

# ======================= Number Buttons =====================
btn_number = []
for i in range(10):
    btn_number.append(Button(width=4, text=str(i), font="times 15 bold", bd=5,
                      command=lambda x=i: enter_number(x)))

btn_text = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn_number[btn_text].place(x=25+j*90, y=70+i*70)
        btn_text += 1

# ======================= Operator Buttons =====================
btn_operator = []
for i in range(4):
    btn_operator.append(Button(width=4, text=str(i), font="times 15 bold", bd=5,
                               command=lambda x=i: enter_operator(x)))

btn_operator[0]['text'] = "+"
btn_operator[1]['text'] = "-"
btn_operator[2]['text'] = "*"
btn_operator[3]['text'] = "/"

for i in range(4):
    btn_operator[i].place(x=290, y=70+i*70)

# =========================== Other Buttons =====================
btn_zero = Button(width=19, text='0', font='times 15 bold', bd=5, command=lambda x=0: enter_number(x))
btn_zero.place(x=25, y=280)

btn_clear = Button(width=4, text='C', font='times 15 bold', bd=5, command=clear_number)
btn_clear.place(x=25, y=350)

btn_dot = Button(width=4, text='.', font='times 15 bold', bd=5, command=lambda x=".": enter_number(x))
btn_dot.place(x=115, y=350)

btn_equal = Button(width=4, text='=', font='times 15 bold', bd=5, command=equal_operator)
btn_equal.place(x=205, y=350)

icon = PhotoImage(file='./icons/delete.png')
btn_delete = Button(width=50, height=35, image=icon, bd=5, command=delete_operator)
btn_delete.place(x=295, y=350)

# ========================= Status Bar======================
status_bar = Label(root, text="History : ", relief="sunken", height=3, anchor=W, font='verdana 11 bold')
status_bar.pack(side=BOTTOM, fill=X)

root.mainloop()
