#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
# define MAX 5

int front=-1,rear=-1;
int arr[MAX];
void enqueue();
void dequeue();

int main(){
int n,ch=1;
while(ch==1){
    printf("choose the operation to perform on queue:\n1.ENQUEUE\n2.DEQUEUE");
    scanf("%d",&n);
    switch(n){
case 1:
    enqueue();
    break;
case 2:
    dequeue();
    break;
default:
    printf("Invalid choice");
    }
    printf("\nif you wish to perform any operation select 1 or select 0");
    scanf("\n%d",&ch);
}
}

void enqueue(){
    int val;
    printf("enter the value to enqueue:");
    scanf("%d",&val);
if(rear==MAX-1){
    printf("Queue is overflow");
}
    else if(rear==-1 && front==-1){
        front=rear=0;
        arr[rear]=val;
    }
    else{
        rear=rear+1;
        arr[rear]=val;
    }
}


void dequeue(){
if(front==-1 || front>rear){
    printf("Queue is underflow");
}
else if(front==rear){
    printf("element dequeued:%d",arr[front]);
    front=rear=-1;
}
else{
   printf("element dequeued:%d",arr[front]);
   front=front+1;
}
}

