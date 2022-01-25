from tkinter import *
from tkinter import ttk


def callback(event):
    item = tree_view.identify('item', event.x, event.y)
    print("You clicked on {}".format(tree_view.item(item, "text")))


root = Tk()
root.geometry('650x650+700+100')
root.title("TreeView")

tree_view = ttk.Treeview(root)
tree_view.pack()

icon = PhotoImage(file='icons/add.png')
tree_view.insert('', 0, 'item1', text='First Item', image=icon)
tree_view.insert('', 1, 'item2', text='Second Item')
tree_view.insert('', 2, 'item3', text='Third Item')
tree_view.insert('', 3, 'item4', text='Fourth Item')
tree_view.move('item3', 'item1', 'end')

tree_view.bind('<Double-1>', callback)

root.mainloop()
