#include<stdio.h>
void push()
{
    int stack[5],i,top=-1,max=100;
    printf("\nenter the element to push\n");
    scanf("%d",&i);
    if(top==max-1)
    {
        printf("stack is full");
    }
    else
    {
        top=top+1;
        stack[top]=i;
    }
    printf("%d",&stack);

    }

void pop()
{
    int stack[100],j,top=-1,max=100;
    if(top==0)
    {
       printf("stack is underflow");
    }
    else
    {
        printf("\npopped element is %d",stack[top]);
        top=top-1;
    }
}

void display()
{
    int top=-1,stack[100];
    if (top!=0)
    {
        printf("\nthe elements of the stack are:\n");
        for(int i=top;i>=0;i++)
        {
            printf("%d",stack[i]);
        }
    }
    else
    {
        printf("stack is empty");
    }
}


void main()
{
    int i=0,ch=1,choice;
    printf("enter your choice:1.push\n2.pop\n3.peek\n4.display");
    scanf("%d",&choice);
    while(choice!=4)
    {
    switch(choice)
    {
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

    default:
        printf("invalid");
        break;
    }
    }
}
