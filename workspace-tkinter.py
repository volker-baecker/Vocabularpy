from tkinter import *
from tkinter.constants import *
root = Tk()
text = Text(root,font=('Tahoma',8))#I need RTL and Right justified text!

text.tag_configure('tag-right', justify='right')
text.insert('end', 'text ' * 10, 'tag-right')
text.grid()

scrl = Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scrl.set)
scrl.grid(row=0, column=1, sticky='ns')
root.mainloop()