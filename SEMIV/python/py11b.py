import pickle
from py11 import student
n=int(input("Enter no. of student:"))
f=open("sd.dat","wb")

for i in range(n):
    print("Enter details of student:")
    nm=input("Enter the name:")
    rn=int(input("Enter the roll no:"))
    ag=int(input("Enter the age:"))
    s=student(rn,nm,ag)
    pickle.dump(s,f)
f.close()
f=open("sd.dat","rb")
while(True):
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print("End of file")
        break
f.close()
