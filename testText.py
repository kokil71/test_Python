from tkinter import *

root = Tk()
text = Text(root)
text.pack()

data = '''Life is too short
You need python'''

text.insert(1.0, data)

root.mainloop()