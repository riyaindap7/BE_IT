class logical_exp:
    def add(self,a,b):
        print("Addition is:",a+b)
    def sub(self,a,b):
        print("Subtraction is:",a-b)
    def multiply(self,a,b):
        print("Multiplication is:",a*b)
    def division(self,a,b):
        print("Division is:",a/b)
t1=logical_exp()
while True:
    print("Choose the operation to perform:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    ch=int(input("Enter your choice:"))
    if ch==1:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        t1.add(a,b)
    elif ch==2:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        t1.sub(a,b)
    elif ch==3:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        t1.multiply(a,b)
    elif ch==4:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        t1.division(a,b)
    else:
        break
        
    
