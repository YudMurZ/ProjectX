from tkinter import *
import ProgramX

root =Tk()

def myClick():
    label1 = Label(root, text="test aja")
    label1.pack()

button1 = Button(root, text="Click Me!", command=myClick)
button1.pack()

root.mainloop()