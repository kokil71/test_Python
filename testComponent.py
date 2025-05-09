from tkinter import *

root = Tk()

listbox = Listbox(root)
label = Label(root, text='제목')
entry = Entry(root)
text = Text(root)
b1 = Button(root, text='생성')
b2 = Button(root, text='수정')
b3 = Button(root, text='삭제')

listbox.grid(row=0, column=0, columnspan=3, sticky='ew')
label.grid(row=1, column=0)
entry.grid(row=1, column=1, columnspan=2, sticky='ew')
text.grid(row=2, column=0, columnspan=3)
b1.grid(row=3, column=0, sticky='ew')
b2.grid(row=3, column=1, sticky='ew')
b3.grid(row=3, column=2, sticky='ew')

root.mainloop()
