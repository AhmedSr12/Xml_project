from tkinter import *
from XmlFile import xmlFile
import tkinter.messagebox

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
        self.err =  self.A.detectErrors()
        self.DetectError_Button = Button(self.master_will_be_deleted, text=" Detect Errors ", command=self.Verifyerror, font="arial 15 italic", width=20)
        self.DetectError_Button.pack(side=BOTTOM)

        #self.correct_Button = Button(self.master_will_be_deleted, text=" Correct Errors ", command=self.B_4_Buttons,font="arial 15 italic", width=20)
        #self.prett_Button = Button(self.master_will_be_deleted, text=" Show Prettified Xml ", command=self.show_prett,font="arial 15 italic", width=20)
        #self.correct_Button.pack(side=BOTTOM)
        #self.correct_Button["state"] = "disabled"

    def Verifyerror(self):
        self.DetectError_Button.destroy()
        self.Master.pack_forget()
        self.Master.destroy()
        if self.err==0:
            self.Master = Frame(self.main)
            self.Master.pack(side=TOP)
            self.show_Label(self.contents)
            tkinter.messagebox.showinfo("ERRORS DETECTED", "No error detected")
            self.B_4_Buttons()
        else:
            self.Master = Frame(self.main)
            self.Master.pack(side=TOP)
            self.show_Label(self.contents)
            string="Number of Detected Errors Equals :"+str(self.err)
            tkinter.messagebox.showinfo("ERRORS DETECTED", string)
            self.B_4_Buttons()
            #self.prett_Button.pack(side=TOP)
            #self.visualize_Button.pack(side=BOTTOM)

    def VisualizeError(self):
        self.Master.pack_forget()
        self.Master.destroy()
        self.Master = Frame(self.main)
        self.Master.pack(side=TOP)
        self.show_Label(self.A.visualizeErrors(),1)
    def delet(self):

        input = self.entry.get()
        if input=="":
            tkinter.messagebox.showinfo("ERROR", "EMPTY ENTRY !")
        else:
            self.Button2["state"] = "normal"
            self.Button1["state"] = "normal"
            self.Button3["state"] = "normal"
            self.Button4["state"] = "normal"
            self.Button5["state"] = "normal"
            self.prett_Button["state"] = "normal"
            output = self.A.word_def(input)
            root = Tk()
            number_of_synsets = Label(root, text=output, font="arial 14 italic")
            number_of_synsets.pack()
            self.Buttonn.destroy()
            self.entry.destroy()
            self.label123.destroy()

    def deletee(self):

        input = self.entry.get()
        if input=="":
            tkinter.messagebox.showinfo("ERROR", "EMPTY ENTRY !")
        else:
            self.Button2["state"] = "normal"
            self.Button1["state"] = "normal"
            self.Button3["state"] = "normal"
            self.Button4["state"] = "normal"
            self.Button5["state"] = "normal"
            self.prett_Button["state"] = "normal"
            output = self.A.Hypernyms_word(input)
            root = Tk()
            number_of_synsets = Label(root, text=output, font="arial 14 italic")
            number_of_synsets.pack()
            self.Buttonn.destroy()
            self.entry.destroy()
            self.label123.destroy()

    def get_def(self):
        self.Button2["state"] = "disabled"
        self.Button1["state"] = "disabled"
        self.Button3["state"] = "disabled"
        self.Button4["state"] = "disabled"
        self.Button5["state"] = "disabled"
        self.prett_Button["state"] = "disabled"
        self.entry=Entry(self._4_buttons_master, font="arial 14 italic")
        self.label123=Label(self._4_buttons_master, text="Enter Tag", font="arial 14 italic")
        self.Buttonn = Button(self._4_buttons_master, text="OK", command=self.delet, font="arial 15 italic",width=10)
        self.Buttonn.grid(row=2, column=5)
        self.entry.grid(row=1, column=4)
        self.label123.grid(row=1, column=3)
    def get_hyper(self):
        self.Button2["state"] = "disabled"
        self.Button1["state"] = "disabled"
        self.Button3["state"] = "disabled"
        self.Button4["state"] = "disabled"
        self.Button5["state"] = "disabled"
        self.prett_Button["state"] = "disabled"
        self.entry=Entry(self._4_buttons_master, font="arial 14 italic")
        self.label123=Label(self._4_buttons_master, text="Enter Query Word", font="arial 14 italic")
        self.Buttonn = Button(self._4_buttons_master, text="OK", command=self.deletee, font="arial 15 italic",width=10)
        self.Buttonn.grid(row=2, column=5)
        self.entry.grid(row=1, column=4)
        self.label123.grid(row=1, column=3)

    def save_as(self):
        pass

    def show_minified(self):
            self.Master.pack_forget()
            self.Master.destroy()
            self.Master = Frame(self.main)
            self.Master.pack(side=TOP)
            self.show_Label(self.A.prettifying())
    def show_prett(self):
        self.Master.pack_forget()
        self.Master.destroy()
        self.Master = Frame(self.main)
        self.Master.pack(side=TOP)
        self.show_Label(self.A.prettifying())
    def number_synsets(self):
        string = "Number Of Synsets equal : " + str(self.A.no_of_synsets())
        tkinter.messagebox.showinfo("Number Of Synsets", string)
    def Json(self):
        self.Master.pack_forget()
        self.Master.destroy()
        self.Master = Frame(self.main)
        self.Master.pack(side=TOP)
        self.show_Label(self.A.json())
        #self.Button1.destroy()

    def B_4_Buttons(self):
        self.master_will_be_deleted.pack_forget()
        self.master_will_be_deleted.destroy()
        self.Master.pack_forget()
        self.Master.destroy()
        self.Master = Frame(self.main)
        self.Master.pack(side=TOP)
        self.show_Label(self.contents)
        self.prett_Button = Button(self._4_buttons_master, text=" Show Prettified Xml ", command=self.show_prett,font="arial 15 italic", width=15)
        self.Button1 = Button(self._4_buttons_master, text=" Show JSON ", command=self.Json, font="arial 15 italic", width=10)
        self.Button2 = Button(self._4_buttons_master, text=" Visualize Error ", command=self.VisualizeError,font="arial 15 italic", width=15)
        self.Button3 = Button(self._4_buttons_master, text=" Get Number Of Synsets ", command=self.number_synsets,font="arial 15 italic", width=20)
        self.Button4 = Button(self._4_buttons_master, text=" Get Definition ", command=self.get_def,font="arial 15 italic", width=10)
        self.Button5 = Button(self._4_buttons_master, text=" Get Hypernyms ", command=self.get_hyper,font="arial 15 italic", width=15)
        self.Button6 = Button(self._4_buttons_master, text=" Show Minified Xml ", command=self.show_minified,font="arial 15 italic", width=20)
        self.Button6.grid(row=0, column=7)
        self.Button5.grid(row=0, column=6)
        self.Button1.grid(row=0, column=5)
        self.Button2.grid(row=0, column=1)
        self.Button3.grid(row=0, column=3)
        self.Button4.grid(row=0, column=4)
        self.prett_Button.grid(row=0, column=2)
        if self.err==0:
            self.Button2["state"] = "disabled"


    def show_Label(self,contents="",type=0):
        fff = open('errorVisualized.txt', 'r')
        listed = fff.readlines()
        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=1200, height=600)

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

        self.text=Text(self.frame,width=1200,height=600)
        self.text.insert(INSERT, contents)
        if type==1:
            for i in range (len(listed)):
                line=listed[i]
                for j in range (len (line)):
                    if j<=len (line)-6:
                        if line[j]=="(":
                            if (line[j+1]=="E") and (line[j+2]=="R") and (line[j+3]=="R") and (line[j+4]==":") :
                                start=str(i+1)+"."+str(j)
                                end=str(i+1)+"."+str(j+5)
                                self.text.tag_add('error', start, end)
                                self.text.tag_config('error',background="yellow", foreground="black")
                                break
        fff.close()
        #self.text=Text(self.frame, text=contents,  relief="solid",font="arial 14 italic",justify=LEFT) (ERR:
        self.text.pack(side=LEFT)




