from tkinter import *
import sqlite3
class MyWindow:
    def __init__(self,root):
        #frame
        self.f=Frame(root,height=700,width=1000)
        self.f.propagate(0)
        self.f.pack()
        #textedit
        self.t1=Label(self.f,text="First Name:")
        self.t2=Label(self.f,text="Last Name:")
        self.t1.grid(row=0,column=0)
        self.t2.grid(row=1,column=0)
        self.t2.grid(row=1,column=0)
        self.t1_entry=Entry(self.f)
        self.t2_entry=Entry(self.f)
        self.t1_entry.grid(row=0,column=1)
        self.t2_entry.grid(row=1,column=1)
        #print(self.first)
        #print(self.last)
        #radiobutton
        self.r0=Label(self.f,text="Gender:")
        self.r1=Radiobutton(self.f,text="MALE",variable=v,value=1)
        self.r2=Radiobutton(self.f,text="FEMALE",variable=v,value=2)
        self.r3=Radiobutton(self.f,text="Other",variable=v,value=3)
        self.r0.grid(row=2,column=0)
        self.r1.grid(row=3,column=0)
        self.r2.grid(row=4,column=0)
        self.r3.grid(row=5,column=0)
        #print(self.gender)
        #drop down menu
        self.d_label=Label(self.f,text="Subject")
        self.d_label.grid(row=6,column=0)
        options=["COA","CNND","EM-4","AT","OS"]
        clicked.set("COA")
        self.drop=OptionMenu(self.f,clicked,*options)
        self.drop.grid(row=6,column=1)
        #print(self.subject)
        #reset button
        self.b1=Button(self.f,text="SAVE",width=10,height=2,command=
                       lambda:self.buttonClick(1))
        self.b2=Button(self.f,text="RESET",width=10,height=2,command=
                       lambda:self.buttonClick(2))
        self.b3=Button(self.f,text="EXIT",width=10,height=2,command=
                       lambda:self.buttonClick(3))
        self.b1.grid(row=7,column=0)
        self.b2.grid(row=8,column=0)
        self.b3.grid(row=9,column=0)
    def buttonClick(self, num):
        if num==1:
            self.save_info()
        if num == 2:
            self.t1_entry.delete(0, END)
            self.t2_entry.delete(0, END)
            v.set(0)  
            clicked.set("COA")
        if num==3:
            root.destroy()
            print("Exiting")
    def save_info(self):
        first=self.t1_entry.get()
        last=self.t2_entry.get()
        gender=v.get()
        subject=clicked.get()
        try:
            conn=sqlite3.connect("exp12.db")
            c=conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS info(firstname TEXT,lastname TEXT,gender TEXT,subject TEXT)")
            c.execute("INSERT INTO info VALUES (?,?,?,?)",(first,last,gender,subject))
            conn.commit()
            conn.close()
            print("saved.")
        except EXCEPTION as e:
            print("error connecting database:",e)
             
root=Tk()
v=IntVar()
clicked=StringVar()
mb=MyWindow(root)
root.mainloop()
