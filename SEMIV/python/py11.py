#to read last two lines
f=open("riya44.txt","r")
str=f.readlines()
lastlines=str[-2:]
print(lastlines)
f.close()
