#include<stdio.h>
#include<malloc.h>

struct node
{
  int info;
  struct node *link;
}*start,*q;

void create_list(int);
void addatbeg(int);
void addafter(int,int);
void del(int);
void display();
void count();
void rev();
void search(int);
void exit();

int main()
{
    //struct node *start,*q; (can be declared here)
    int choice,n,m,position,i;
    start=NULL;
    while(1)
    {
      printf("1.create list\n");
      printf("2.add at beginning\n");
      printf("3.add after\n");
      printf("4.delete\n");
      printf("5.display\n");
      printf("6.count\n");
      printf("7.reverse");
      printf("8.search\n");
      printf("9.out\n");
      printf("enter your choice:");
      scanf("%d",&choice);
      switch(choice)
      {
      case 1:
        printf("how many nodes you want:");
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            printf("enter the element:");
            scanf("%d",&m);
            create_list(m);
        }
        break;
      case 2:
          printf("enter the element:");
          scanf("%d",&m);
          addatbeg(m);
          break;
      case 3:
          printf("enter the element:");
          scanf("%d",&m);
          printf("Enter the position after which this element is inserted:");
          scanf("%d",&position);
          addafter(m,position);
          break;
      case 4:
          if(start==NULL)
          {
              printf("Stack is underflow\n");
              continue;
          }
          printf("enter the element for deletion:");
          scanf("%d",&m);
          //del(m);
          break;
      case 5:
        //display();
        break;
      case 6:
        // count();
         break;
      case 7:
         //rev();
         break;
      case 8:
          printf("Enter the element to be searched:");
          scanf("%d",&m);
          //search(m);
          break;
      case 9:
          //exit();
          break;
      default:
        printf("wrong choice\n");
        break;


      }
    }
}

void create_list(int data)
{
    struct node *temp;
    temp=malloc(sizeof(struct node));
    temp->info=data;
    temp->link=NULL;
    if(start==NULL)
    {
        start=temp;
    }
    else{
        q=start;
        while(q->link!=NULL)
        {
         q=q->link;
         q->link=temp;
        }
    }
}

void addatbeg(int data)
{
    struct node *temp;
     temp=malloc(sizeof(struct node));
    temp->info=data;
    temp->link=start;
    start=temp;
}

void addafter(int data,int pos)
{
    struct node *temp,*q;
    int i;
    q=start;
    for(i=0;i<pos-1;i++)
    {
        q=q->link;
        if(q==NULL)
        {
            printf("there are than %d elements",pos);
            return;
        }
    }

    temp=malloc(sizeof(struct node));
    temp->link=q->link;
    temp->info=data;
    q->link=temp;
}
