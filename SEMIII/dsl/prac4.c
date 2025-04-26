#include<stdio.h>
#include<stdlib.h>

struct node{
int data;
struct node *next;
};
struct node *front=0;
struct node *rear=0;

void enqueue();
void dequeue();
void display();

int main(){
int n,choice=1;
while(choice==1){
    printf("\nenter what you wish to do with queue:\nENQUEUE\n2.DEQUEUE\n3.DISPLAY\n");
    scanf("%d",&n);
    switch(n){
case 1:
    enqueue();
    break;
case 2:
    dequeue();
    break;
case 3:
    display();
    break;
default:
    printf("wrong choice");
    }
}
return 0;
}

void enqueue(){
int num;
printf("enter number:");
scanf("%d",&num);
struct node *newnode;
newnode=(struct node *)malloc(sizeof(struct node));
newnode->data=num;
newnode->next=0;
if(front==0&& rear==0){
    front=rear=newnode;
}
else{
    rear->next=newnode;
    rear=newnode;
}
}

void display(){
struct node *temp;
temp=front;
printf("%d\t",temp->data);
temp=temp->next;
}

void dequeue(){
struct node *temp;
temp=front;
if(front==0 && rear==0){
    printf("nil");
}else{
printf("dequeued element is: %d",temp->data);
front=temp->next;
free(temp);
}

}
