#include<stdio.h>
#define MAX 5
int queue_arr[MAX];
int rear = -1;
int front = -1;
void enqueue();
void dequeue();
void display();



int main()
{
  int i;
  while(1)
{
  printf("\nenter a choice:\n1.enqueue\n 2.dequeue\n 3.display\n");
  scanf("%d",&i);
  switch(i)
  {
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
        break;
  }

}
 return 0;
}

void enqueue()
{
    int val;
    printf("enter the value to insert:\n");
    scanf("%d",&val);
    if(rear==MAX-1)
    {
        printf("\nqueue is overflow");
    }
    else
    {
        if(rear==-1 && front==-1)
        {
            front=rear=0;
            queue_arr[rear]=val;
        }
        else
        {
            rear=rear+1;
            queue_arr[rear]=val;
        }
    }
}

void dequeue()
{
    int val;
    if(front==-1 || front>rear)
    {
     printf("\nqueue is underflow");

    }
    else if(front==rear)
   {
     val=queue_arr[front];
     printf("\n%d",val);
     front=front+1;
     front=rear=-1;
   }
   else
   {
     val=queue_arr[front];
     front=front+1;
   }
}

void display()
{
    if(front==-1)
    {
        printf("\nqueue is empty");
    }
    else{
      for(int i=front;i<=rear;i++)
        {
            printf("%d",queue_arr[i]);
        }
    }
}
