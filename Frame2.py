from tkinter import *
from XmlFile import xmlFile

class frame2():
    def __init__(self,master,filePath,contents):
        self.contents=contents
        self.main=master
        self.Master = Frame(master)
        self.Master.pack(side=TOP)
        self.master_will_be_deleted = Frame(master)
        self.master_will_be_deleted.pack(side=BOTTOM)
        self._4_buttons_master = Frame(self.main)
        self._4_buttons_master.pack(side=BOTTOM)
        self.path=filePath
        self.A = xmlFile()
        self.A.addFile(contents)
        self.A.extractlists()
        self.A.extractDeclerations()
        self.A.mergeComments()
        self.A.createTree()
        err =  self.A.detectErrors()
        self.vis_Button = Button(self.master_will_be_deleted, text=" Detect Errors ", command=self.Verifyerror, font="arial 15 italic", width=20)
        self.vis_Button.pack(side=BOTTOM)

        self.correct_Button = Button(self.master_will_be_deleted, text=" Correct Errors ", command=self.B_4_Buttons,font="arial 15 italic", width=20)
        self.correct_Button.pack(side=BOTTOM)
        self.correct_Button["state"] = "disabled"

    def Verifyerror(self):
        self.vis_Button["state"] = "disabled"
        self.correct_Button["state"] = "normal"
        self.Master.pack_forget()
        self.Master.destroy()
        # h3ml if condition 34an a4of fe errors aslun wla la2 fn b4 buttons
        # ha5od el error visualized fn we trg3li string mn m7mod
        self.Master = Frame(self.main)
        self.Master.pack(side=TOP)
        self.show_Label("de7k bela hadf")

    def Errors(self):
        pass
        # new string is needed
    def Json(self):
        self.Master.pack_forget()
        self.Master.destroy()
        self.Master = Frame(self.main)
        self.Master.pack(side=TOP)
        self.show_Label(self.A.json())
        self.Button1.destroy()

    def B_4_Buttons(self):
        self.master_will_be_deleted.pack_forget()
        self.master_will_be_deleted.destroy()
        self.Master.pack_forget()
        self.Master.destroy()
        # ha5od el correct error  fn we trg3li string mn m7mod
        self.Master = Frame(self.main)
        self.Master.pack(side=TOP)
        self.show_Label("de7k bela hadf klaket tany mara")
        self.Button1 = Button(self._4_buttons_master, text=" Show JSON ", command=self.Json, font="arial 15 italic", width=20)
        self.Button2 = Button(self._4_buttons_master, text=" Show Prettified xml ", command=self.Errors,font="arial 15 italic", width=20)
        self.Button3 = Button(self._4_buttons_master, text=" Show De7k ", command=self.Errors,font="arial 15 italic", width=20)
        self.Button1.grid(row=0, column=1)
        self.Button2.grid(row=0, column=2)
        self.Button3.grid(row=0, column=3)

    def show_Label(self,contents=""):
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

        #print(contents)
        #contents="De7k bela hdff"
        self.text=Text(self.frame,width=1250, height=800)
        self.text.insert(INSERT, contents)
        #self.text=Text(self.frame, text=contents,  relief="solid",font="arial 14 italic",justify=LEFT)
        self.text.pack(side=LEFT)




