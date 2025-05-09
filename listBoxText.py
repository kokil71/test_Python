from tkinter import *

root = Tk()
listbox = Listbox(root)
listbox.pack()

for i in ['one', 'two', 'three', 'four']:
    listbox.insert(END, i)

def event_for_listbox(event):
    print("Hello Event")

listbox.bind('<<ListboxSelect>>', event_for_listbox)

root.mainloop()