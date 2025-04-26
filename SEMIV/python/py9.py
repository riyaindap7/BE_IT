class queue1:
    def __init__(self):
        self.rear=-1
        self.front=-1
        self.size=5
        self.l=[]
    
    def enqueue(self,element):
        if(self.rear==self.size-1):
            print("overflow")
        elif(self.front==-1 and self.rear==-1):
            self.front=0
            self.rear=self.rear+1
            self.l.append(element)
            print(self.l)
        else:
            self.rear=self.rear+1
            self.l.append(element)
            print(self.l)

    def rotate(self):
        n = int(input("Enter no. of rotations: "))
        self.l = self.l[n % len(self.l):] + self.l[:n % len(self.l)]
        print("Queue rotated by", n, "steps:", self.l)
        
    def dequeue(self):
        if(self.front==-1 or self.front>self.rear):
            print("underflow")
        else:
            print("Element deleted from queue:", self.l[self.front])
            self.l.pop(self.front)
            self.front=self.front+1
            print(self.l)
    def extend(self,elements):
        self.l.extend(elements)
        print(self.l)
        
  

a1=queue1()
while True:
    print("Choose the operation to perform:")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.rotate")
    print("4.extend")
    ch=int(input("Enter your choice:"))
    if ch==1:
        element=int(input("enter element to add in queue:"))
        a1.enqueue(element)
    elif ch==2:
        a1.dequeue()
    elif ch==3:
        a1.rotate()
    elif ch==4:
         elements = list(map(int, input("Enter the elements to extend the queue (comma-separated): ").split(',')))
         a1.extend(elements)
    else:
        break
