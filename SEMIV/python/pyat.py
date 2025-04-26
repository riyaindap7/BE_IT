def find_min():
    print("To find min of two numbers")
    num1=int(input("Enter a number:"))
    num2=int(input("Enter another number:"))
    if(num1>num2):
        print("Number {} is minimum amongst {} & {}".format(num2,num1,num2))
    else:
        print("Number {} is minimum amongst {} & {}".format(num1,num1,num2))
    print("------------------------------------------")
 
def reverse():
    print("To reverse a number")
    num=int(input("Enter a number:"))
    print("Entered number is:{}".format(num))
    rev=0
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print("Reversed number is:{}".format(rev))
    print("------------------------------------------")

def armstrong():
    print("To find armstrong number")
    num=(int(input("Enter a number:")))
    og=str(num)
    armstg=0
    for i in og:
        digit=(num)%10
        armstg=armstg+(digit)**len(str(og))
        num=(num)//10
    print(armstg)
    if(int(og)==armstg):
        print("The number {} is an armstrong number".format(og))
    else:
        print("The number {} is not an armstrong number".format(og))
    print("------------------------------------------")

def slicing():
    list1=[]
    for i in range(10):
        num=int(input(f"Enter num{i+1}:"))
        list1.append(num)
#extracting 4th element
    print("The 4th element in list is:",list1[3])
#extracting all elements from 6th
    print("All elements from 6th element are:",list1[5: ])
#extracting last five elements in reverse
    print("The last five elements in reverse :",list1[-1:-6:-1])
    print("------------------------------------------")

def pattern_printing():
    n=4
    for i in range (n,0,-1):
        for j in range(1,i+1):
            print(2*j,end=" ")
        print("\n")
    print("------------------------------------------")
        
class Main:
    while True:
        print("Choose the question number to be solved:")
        print("1)Find min of two numbers read from the user \n2)Read a number from the user and Perform the reverse of a number \n3)Calculate Armstrong of a number entered by the user  \n4)Pattern printing \n   2 4 6 8 \n   2 4 6\n   2 4\n   2 \n5)Declare a list of 10 items and perform slicing \n i)extract 4th element \n ii)extract all elements from 6th element \n iii)extract last five elements in reverse order")
        ch=input("Enter choice number(or q to quit):")
        print("------------------------------------------")
        if ch=='1':
            find_min()
        elif(ch=='2'):
            reverse()
        elif(ch=='3'):
            armstrong()
        elif(ch=='4'):
            pattern_printing()
        elif(ch=='5'):
            slicing()
        elif(ch.lower()=='q'):
            break
        else:
            print("Invalid input")

    

    
