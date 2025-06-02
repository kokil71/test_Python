from tkinter import *

root = Tk()
b1 = Button(root, text='테스트')
b1.pack()

def btn_click(event):
    print("버튼이 클릭되었습니다")

#b1.bind('<Button-1>', btn_click)
#b1.bind('<Button-2>', btn_click)
b1.bind('<Button-3>', btn_click)

root.mainloop()