#include<stdio.h>
#include<stdlib.h>

struct node{
  int data;
  struct node *next;
};
struct node *top=0;
struct node *newnode;
struct node *temp;
void push();
void pop();
void peek();
void display();

int main(){
int n,choice=1;
while(choice==1){
    printf("what you wish to do on stack:\n1.Push\n2.POP\n3.PEEK\n4.DIsplay\n");
    scanf("%d",&n);
    switch(n){
case 1:
    push();
    break;
case 2:
    pop();
    break;
case 3:
    //peek();
    break;
case 4:
    display();
    break;
case 5:
    printf("enter  avalid choice");
    break;

    }
    printf("\nyou wish to continue:(0,1)\n");
    scanf("%d",&choice);
}
return 0;
}

void push(){
int num;
printf("enter the element to push in stack:");
scanf("%d",&num);
struct node *newnode=(struct node*)malloc(sizeof(struct node));
//struct node *top=0;
newnode->data=num;
newnode->next=top;
top=newnode;

}

void pop(){
    struct node *temp;
    temp=top;
if(top==0){
    printf("nil");
}else{
printf("popped element is: %d",top->data);
top=top->next;
free(temp);

}
}
void peek(){
if(top==0){
    printf("nil");
}else{
printf("popped element is: %d",top->data);
}

void display(){
struct node *temp=top;
while(temp!=0){
    printf("%d",temp->data);
    temp=temp->next;
}
printf("\n");
}
