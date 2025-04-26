#Q.9
"""x=float(input("Enter a number:"))
if x%2==0:
    print(f"{x} is a even number")
else:
    print(f"{x} is a odd number")"""

#Q.10
"""x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
print("Checking for comparison operator:")
if x==y:
    print(f"{x} and {y} are equal numbers")
elif x!=y:
    print(f"{x} and {y} are not equal numbers")
elif x>y:
    print(f"{x} is greater than {y}")
elif x<y:
    print(f"{x} is less than {y}")
elif x>=y:
    print(f"{x} is greater than or equal to {y}")
elif x<=y:
    print(f"{x} is less than or equal to {y}")

print("----")
print("Checking for logical operator:")
if x>5 and y<10:
    print("and operation is true")
else:
    print("and operation is false")
if x>5 or y<10:
    print("or operation is true")
else:
    print("or operation is false")
if not(x>5 and y<10):
    print("not operation is true")
else:
    print("not operation is false")"""

#Q.11
"""x=float(input("Enter a number:"))
if x>0:
    print(f"{x} is a positive number")
elif x<0:
    print(f"{x} is a negative number")
else:
    print(f"{x} is a zero.")"""

#Q.12
"""print("Enter marks out of 100")
x=float(input("Enter Physics's marks:"))
y=float(input("Enter Chemistry's marks:"))
z=float(input("Enter Maths's marks:"))
avg=(x+y+z)/3
if avg>50:
    print("You have passed the examination")
else:
    print("You have failed the examination")"""

#Q.13
"""year=int(input("Enter a year to check if leap or not:"))
if (year%4==0 and year%100!=0)or (year%100==0 and year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")"""

#Q.14
"""unit=int(input("Enter units consumed:"))
if unit<=10:
    print("As your consumed units are less than 10 ,no bill is charged")
elif unit<=100:
    unit1=unit-10
    bill=unit1*5
    print(f"Your bill is {bill} rs")
elif unit>100 and unit<=200:
    unit1=unit-110
    bill=(100*5)+(unit1*10)
    print(f"Your bill is {bill} rs")
else:
    unit1=unit-210
    bill=(100*5)+(100*10)+(unit1*15)
    print(f"Your bill is {bill} rs")"""

#Q.15
"""x=float(input("Enter 1st number:"))
y=float(input("Enter 2nd number:"))
z=float(input("Enter 3rd number:"))
if x>y and x>z:
    print(f"{x} is greatest among three")
elif y>z and y>x:
    print(f"{y} is greatest among three")
else:
    print(f"{z} is greatest among three")"""

#Q.16
"""for i in range(101):
    print(i)

i=1
while i<=100:
    print(i)
    i+=1"""

#Q.17
"""n=int(input("Enter value of n:"))
n1=n
sum1=0
while n>=0:
    sum1=sum1+n
    n-=1
print(f"Sum of natural numbers till {n1} is {sum1}")
sum2=0
for i in range(1,n1+1):
    sum2=sum2+i
print(f"Sum of natural numbers till {n1} is {sum2}")"""

#Q.18
"""for i in range(1,11):
    print(f"for student{i}:")
    name=input("Enter name:")
    x=int(input("Enter marks for sub1:"))
    y=int(input("Enter marks for sub2:"))
    z=int(input("ENter marks for sub3:"))
    print("Total of three subj is :",(x+y+z))
    avg=(x+y+z)/3
    if avg>50:
        print(f"{name} has passed the examination")
    else:
        print(f"{name} has failed the examination")"""

#Q.19
"""for i in range(5):
    for j in range(1,i*2+2,2):
        print(chr(65+j-1),end=" ")
    print("")"""

#Q.20
"""for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()"""

#Q.21
"""i=0
j=1
count=10
while(count>=0):
    print(i)
    i,j=j,j+i
    count-=1
i=0
j=1
for count in range(11,0,-1):
    print(i)
    i,j=j,j+i"""

#Q.22
"""num=int(input("ENter number to find factorial:"))
num1=num
facto=1
for i in range(1,num+1):
    facto=facto*i
print(f"factorial of {num1} is {facto}")"""

#Q.23
"""num=int(input("Enter a number:"))
num_str=str(num)
print(num_str[::-1])
if num_str==num_str[: :-1]:
    print("Entered string is palindrome")
else:
    print("Entered string is not a palindrome")
rev=0
while num>0:
    rem=num%10
    num=num//10
    rev=rev*10+rem
print(rev)"""

#Q.24
"""i=2
while i<=100:
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime:
        print(i)
    i+=1"""

#Q.25
"""import array as arr
arr1=[]
size=int(input("ENter size of array:"))
for i in range(size):
    num=int(input(f"ENter element{i+1}:"))
    arr1.append(num)
print(f"Array is:{arr1}")
thrice=[i*3 for i in arr1]
print(f"Thrice of Array is:{thrice}")
print("printing elements 2 to 4:",arr1[2:5])
print("Element at index 3:",arr1[3])"""

#Q.26
"""arr=[]
while True:
    print("ENter operation to perform on stack:")
    print("1)PUsh \n 2)Pop \n 3)Display \n 4)exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        num=int(input("ENter element to push:"))
        arr.append(num)
    if ch==2:
        arr.pop()
    if ch==3:
        print(arr)
    if ch==4:
        break
    else:
        print("ENter a vaild choice")"""

#Q.27
"""arr=[]
size=int(input("Enter size of array:"))
for i in range(size):
    arr.append(int(input()))
num=int(input("ENter the element to search for:"))
flag=False
for i in range(len(arr)):
    if arr[i]==num:
        flag=True

if flag:
    print("Element found")
else:
    print("Element not found")"""

#Q.28
"""arr=[]
size=int(input("Enter size of array:"))
for i in range(size):
    arr.append(int(input()))
n=int(input("Enter element to search for:"))
left=0
right=len(arr)-1
result=-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==n:
        result=mid
        break
    elif arr[mid]<n:
        left=mid+1
    else:
        right=mid-1

if result!=-1:
    print(f"Element found at index {result}")
else:
    print("Element not found")"""

#Q.30
"""ch=int(input("Enter a choice between 1 to 5 to check exception:"))
if ch==1:
    try:
        a=int(input("A value:"))
        b=int(input("B value:"))
        c=a/b
        print(f"{a}\{b}={c}")
    except ZeroDivisionError:
        print("dividion by zero!")
if ch==2:
    try:
        a=int(input("A value:"))
        b=int(input("B value(enter a char):"))
        c=a/b
        print(f"{a}\{b}={c}")
    except ValueError:
        print("Wrong type of input")
if ch==3:
    try:
        a=int(input("A value:"))
        b=int(input("B value(enter a char):"))
        c=a/k
        print(f"{a}\{b}={c}")
    except NameError:
        print("Division by wrong variable")
if ch==4:
    try:
        a='2'
        b=5
        c=a+b
    except TypeError:
        print("Operation on wrong type of vari")
if ch==5:
    try:
        n=int(input("ENter no btw 2 to 5:"))
        assert n>=2 and n<=5
        print(n)
    except:
        print("Assertion error")"""

#Q.30
"""sum=lambda a,b:a+b
print(sum(23,0))

max=lambda a,b:a if (a>b) else b
print(max(11,12))

num=lambda a:print("Even") if a%2==0 else print("odd")
print(num(9))

lst=[[1,3,2],[5,4,7,6],[9,8]]
sortlist=lambda x:(sorted(i) for i in x)
for sorted_sublist in sortlist(lst):
    print(sorted_sublist)

pets=["dog","cat","camel","zebra"]
stray_pets=list(map(str.upper,pets))
print(stray_pets)

rounding=[1.245789,3.564789876,4.34567,5.23456456,6.34567890456]
rounded=list(map(round,rounding,range(1,7)))
print(rounded)

strings=['a','b','c','d','e','f']
nums=[1,2,3,4,5,6,7]
new=list(map(lambda x,y:(x,y),strings,nums))
print(new)"""

#Q.a
"""class Student:
    def __init__(self):
        self.name=input("ENter your name:")
        self.branch=input("Enter branch:")
        #self.marks=self.Marks()
    def display(self):
        print(self.name,"," ,self.branch)

    class Marks:
        def __init__(self):
            self.sub1=int(input("ENter sub1 marks:"))
            self.sub2=int(input("ENter sub2 marks:"))

        def total(self):
            total=(self.sub1+self.sub2)//2
            print("total=",total)
        def percentage(self):
            per=(self.sub1+self.sub2)*100//200
            print("perc=",per)
s1=Student()
s1.display()
s=s1.Marks()
s.total()
s.percentage()"""

#Q.b
"""class circle:
    def __init__(self):
        self.r=int(input("ENter value of radius:"))

    def area(self):
        area=3.14*self.r*self.r
        print("area=",area)

    def perimeter(self):
        per=2*3.14*self.r
        print("perimeter=",per)
c1=circle()
c1.area()
c1.perimeter()"""

#Q.c
"""class Bank:
    def __init__(self):
        self.balance=0
        print("balance initally:",self.balance)

    def deposit(self):
        d=int(input("ENter deposit amount="))
        self.balance=self.balance+d
        print("bal aft depos=",self.balance)
    def withdrawal(self):
        if self.balance==0:
            print("Nothing to withdraw")
        else:
            w=int(input("Enter money to with"))
            self.balance=self.balance-w
            print("money after with=",self.balance)
e1=Bank()
e1.deposit()
e1.withdrawal()"""

#Q.d
"""class Employee:
    n=0
    def __init__(self):
        self.empid=int(input("ENter empid:"))
        self.dep=input("ENter dept:")
        self.salary=float(input("Enter salary:"))
        Employee.n=Employee.n+1
    def display(self):
        print(f"For empid {self.empid}:")
        print(self.dep)
        print(self.salary)
    def update(self,salary):
        self.salary=salary
        print("update salary:",self.salary)
    @classmethod
    def count(cls):
        print("Total emp:",cls.n)

class Manager(Employee):
    pass
class Staff(Employee):
    pass
m1=Manager()
m1.display()
m1.update(200000)
s1=Staff()
s1.display()
s1.count()"""

#Q.e
"""from abc import ABC,abstractmethod

class college:
    @abstractmethod
    def collegename(self):
        print("college name is:SFIT")
    def dept(self):
        print("Department name is: INFT")
    def perf(self):
        pass

class student(college):
    def name(self):
        x=input("enter your name:")
        print("hey {}".format(x))
    def perf(self):
        x=int(input("enter your cgpa:"))
        if x>=6:
            print("Your perfomance is satisfactory!\n")

class teacher(college):
    def perf(self):
        x=int(input("enter your experience:"))
        if x>=5:
            print("you are experienced!")

s1=student()
s1.collegename()
s1.dept()
s1.perf()

t1=teacher()
t1.collegename()
t1.dept()
t1.perf()"""

#Q.f
"""from multipledispatch import dispatch

class calculate:
    @dispatch(int)
    def area(self,radius):
        print("Area of circle:",3.14*radius*radius)

    @dispatch(int,int)
    def area(self,leng,base):
        print("Area of triangle:",0.5*leng*base)

    @dispatch(int,int,int)
    def area(self,leng,brea,one):
        print("Area of rect:",leng*brea*one)
c=calculate()
c.area(2)
c.area(6,2)
c.area(2,6,1)"""

#Q.g
from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def push(self, element):
        self.queue.append(element)
        print("Pushed element", element, "to the rear of the queue.")
    def pop(self):
        if len(self.queue) == 0:
            print("Queue is empty. Cannot pop from an empty queue.")
            return None
        else:
            element = self.queue.popleft()
            print("Popped element", element, "from the front of the queue.")
            return element
    def rotate(self, steps):
        self.queue.rotate(steps)
        print("Queue rotated", steps, "steps.")
    def extend(self, elements):
        self.queue.extend(elements)
        print("Extended queue with elements:", elements)
    def display(self):
        print("Current Queue:", list(self.queue))
q = Queue()
while True:
    print("\nMenu:")
    print("1. Push element to the rear")
    print("2. Pop element from the front")
    print("3. Rotate queue")
    print("4. Extend queue")
    print("5. Display queue")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        element = int(input("Enter the element to push: "))
        q.push(element)
    elif choice == '2':
        q.pop()
    elif choice == '3':
        steps = int(input("Enter the number of steps to rotate: "))
        q.rotate(steps)
    elif choice == '4':
        elements = list(map(int, input("Enter the elements to extend the queue (comma-separated): ").split(',')))
        q.extend(elements)
    elif choice == '5':
        q.display()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


        
        
        


        
    
    
    

              
    
  
    
