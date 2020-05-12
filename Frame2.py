from tkinter import *

class frame2():
    def __init__(self,master,filePath):
        self.Master = master
        self.master_will_be_deleted = Frame(master)
        self.master_will_be_deleted.pack(side=BOTTOM)
        self._4_buttons_master = Frame(self.Master)
        self._4_buttons_master.pack(side=BOTTOM)
        self.path=filePath
        self.vis_Button = Button(self.master_will_be_deleted, text=" Verify Consistency ", command=self.error, font="arial 15 italic", width=20)
        self.vis_Button.pack(side=BOTTOM)

        self.correct_Button = Button(self.master_will_be_deleted, text=" Correct Errors ", command=self.B_4_Buttons,font="arial 15 italic", width=20)
        self.correct_Button.pack(side=BOTTOM)
        self.correct_Button["state"] = "disabled"
    def error(self):
        self.correct_Button["state"] = "normal"
    def Errors(self):
        pass
        # new string is needed
    def B_4_Buttons(self):
        self.master_will_be_deleted.pack_forget()
        self.master_will_be_deleted.destroy()
        self.Button1 = Button(self._4_buttons_master, text=" Show corrected ", command=self.Errors, font="arial 15 italic", width=20)
        self.Button2 = Button(self._4_buttons_master, text=" Show JSON ", command=self.Errors,font="arial 15 italic", width=20)
        self.Button3 = Button(self._4_buttons_master, text=" Show? ", command=self.Errors,font="arial 15 italic", width=20)
        self.Button4 = Button(self._4_buttons_master, text=" Show?? ", command=self.Errors,font="arial 15 italic", width=20)
        self.Button1.grid(row=0, column=1)
        self.Button2.grid(row=0, column=2)
        self.Button3.grid(row=0, column=3)
        self.Button4.grid(row=0, column=4)

    def show_Label(self):
        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=1250, height=800)

        canvas = Canvas(self.Master)
        self.scroll = Frame(self.Master)
        self.scroll.pack(side=BOTTOM,fill="x")
        self.frame = Frame(canvas)
        myscrollbar = Scrollbar(self.Master, command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", myfunction)
        myscrollbar.pack(side=RIGHT,fill="y")
        canvas.pack(side=RIGHT)



        myscrollbar1 = Scrollbar(self.scroll, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=myscrollbar1.set)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", myfunction)
        myscrollbar1.pack(side="bottom", fill="x")
        canvas.pack(side="bottom")

        f=open(self.path,"r")
        contents=f.read()
        #print(contents)
        #contents="De7k bela hdff"
        self.text=Text(self.frame,width=1250, height=800)
        self.text.insert(INSERT, contents)
        #self.text=Text(self.frame, text=contents,  relief="solid",font="arial 14 italic",justify=LEFT)
        self.text.pack(side=LEFT)




