"""from tkinter import *
class MyButton:
    def __init__(self,root):
        #create a frame as child to root window
        self.f=Frame(root,height=400,width=500)
        self.f.propagate(0)
        self.f.pack()
        #create three push buttons
        self.b1=Button(self.f,text="RED",width=15,height=2,
                       command=lambda: self.buttonClick(1))
        self.b2=Button(self.f,text="GREEN",width=15,height=2,
                       command=lambda: self.buttonClick(2))
        self.b3=Button(self.f,text="PINK",width=15,height=2,
                       command=lambda: self.buttonClick(3))
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
    def buttonClick(self,num):
        if num==1:
            self.f["bg"]="red"
        if num==2:
            self.f["bg"]="green"
        if num==3:
            self.f["bg"]="pink"
root=Tk()
mb=MyButton(root)
root.mainloop()"""

import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
# Load images
image = tk.PhotoImage(file="C://Users//RIYA//OneDrive//Pictures//socialmedia2.png")
# Create image button
button = tk.Button(root, image=image, command=lambda: messagebox.showinfo("Message", "Button clicked"))
button.pack()
root.mainloop()

           
