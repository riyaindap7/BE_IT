#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define MAX 5
int top=-1;
int arr[MAX];
void push();
void pop();
void peek();

int main(){
int arr[MAX];
int n,ch=1,top=-1;
while(ch==1){
printf("choose the operation to perform on Stack:\n1.PUSH\n2.POP\n3.PEEK \n");
scanf("%d",&n);
switch(n){
case 1:
push();
break;
case 2:
pop();
break;
case 3:
peek();
break;

}
printf("\nif you wish to perform any operation select 1 or select 0");
scanf("\n%d",&ch);
}
}

void push()
{
int val;
printf("\nenter the element to push on stack:");
scanf("%d",&val);
if(top==4){
printf("Stack is overflow ");
}
else{
top=top+1;
arr[top]=val;
}
}


void pop()
{
if(top==-1){
printf("stack is underflow");
}
else{
printf("\npopped element is : %d",arr[top]);
top=top-1;
}
}

void peek(){
if(top==-1){
printf("Stack is empty");
}
else{
printf("topmost element is : %d",arr[top]);
}
}



