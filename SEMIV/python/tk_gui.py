"""from tkinter import *
from PIL import ImageTk, Image
#create root window
root = Tk()

#set window title
root.title("My window")

#set window size
root.geometry("400x600")

#create canvas to create the drawing
c=Canvas(root, bg="#4169E1",width=400,height=600)

#after creation, add it to root window
c.pack()

#create an oval
id= c.create_oval(0,-200,400,200, width=5, fill="#30D5C8", outline="#30D5C8")
id= c.create_oval(150, 140, 250, 240, width=5, fill="white", outline="white")

#create some text
fnt=("Livic",30,"bold")
id=c.create_text(200, 450, tex="TO DO LIST", font=fnt, fill="white")

#create image
try:
    image = Image.open("C:/Users/RIYA/Downloads/g1 (1).png")
    image = ImageTk.PhotoImage(image)
    image_id = c.create_image(200, 200, anchor="center", image=image)
except FileNotFoundError:
    print("Image file not found.")

c.pack()
#wait and watch for any events that may take place
root.mainloop()"""

import sqlite3
conn=sqlite3.connect("empl.db")
c=conn.cursor()
c.execute("CREATE TABLE emp(firstname TEXT,lastname TEXT,PAY INTEGER)")
c.execute("INSERT INTO emp VALUES ('Riya','INdap',1000000)")
c.execute("INSERT INTO emp VALUES ('Om','I',100000)")
c.execute("INSERT INTO emp VALUES ('Sachi','J',100000)")
c.execute("INSERT INTO emp VALUES ('S','B',100000)")
conn.commit()
c.execute('SELECT * FROM emp WHERE lastname="I"')
print(c.fetchone())
print("------------------")
c.execute('SELECT * FROM  emp')
print(c.fetchall())
conn.commit()
conn.close()

