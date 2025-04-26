num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
if num1>num2 and  num1>num3:
    print("number {} is greatest among three".format(num1))
elif num2>num1 and num2>num3:
    print("number {} is greatest among three".format(num2))
else:
    print("number {} is greatest among three".format(num3))
    
    
    
