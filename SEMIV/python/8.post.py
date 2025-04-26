from abc import ABC,abstractmethod

class college:
    @abstractmethod
    def collegename(self):
        print("college name is:SFIT")
    def dept(self):
        print("Department name is: INFT")
    def perf(self):
        pass

class student(college):
    """def name(self):
        x=input("enter your name:")
        print("hey {}".format(x))"""
    def perf(self):
        x=float(input("enter your cgpa:"))
        if x>=6.00:
            print("Your perfomance is satisfactory!\n")

class teacher(college):
    def perf(self):
        x=int(input("enter your experience:"))
        if x>=5:
            print("you are experienced!")
print("'Hey i am student'")
s1=student()
s1.collegename()
s1.dept()
s1.perf()
print("---------------------")
print("'Hey i am teacher'")
t1=teacher()
t1.collegename()
t1.dept()
t1.perf()
