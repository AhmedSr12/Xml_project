from tkinter import *
from  Frame1 import  frame1
root=Tk()
root.title("Xml Editor")
f=Frame(root)
f.pack()
i=frame1(f)
def reset():
    global f
    f.pack_forget()
    f.destroy()
    f = Frame(root)
    f.pack()
    i = frame1(f)
reset_b = Button(root, text=" Reset ", command=reset,width=5 , height= 1,font="arial 12 italic")
reset_b.pack(side=BOTTOM)
root.mainloop()