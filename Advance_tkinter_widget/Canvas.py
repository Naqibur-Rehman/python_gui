from tkinter import *

root = Tk()
root.geometry('500x450+750+100')
root.title("Canvas")

canvas = Canvas(root, width=500, height=450)
canvas.pack()

# line = canvas.create_line(100, 300, 450, 20)
# canvas.itemconfigure(line, fill='red', width=5)

# line2= canvas.create_line(25, 50, 150, 150, 250, 140, 25, 50, fill='turquoise', width=3)

# text = canvas.create_text(80, 100, text='Naqeeb', font=("Times", 30, 'bold'))

rectangle = canvas.create_rectangle(150, 150, 250, 200, fill='Green', width=5)

oval = canvas.create_oval(350, 350, 250, 200)

arc = canvas.create_arc(120, 20, 30, 80, fill='red', width=3, start=0, extent=180)

icon = PhotoImage(file='icons/add.png')
image = canvas.create_image(150, 200, image=icon)

canvas.lift(rectangle)

root.mainloop()
