#include<stdio.h>
#include<stdbool.h>
struct node{
int data;
struct node *next;
};

struct node *head=0,*temp,*newnode;
int count=0;
void create_list();
void addatbeg();
void delfrbeg();
void addbtw();
void delatend();
void reverse();
void search();
int display();

int main(){
int n,ch=1;
while(ch==1){
    printf("\nlinked list operation:\n1.creating a list\n2.add at beginning\n3.delete from beginning\n4.add in between\n5.delete from end\n6.revserving\n7.search for a node:\n8.display\n");
    scanf("%d",&n);
    switch(n){
case 1:
    create_list();
    break;
case 2:
    addatbeg();
    break;
case 3:
    delfrbeg();
    break;
case 4:
    addbtw();
    break;
case 5:
    delatend();
    break;
case 6:
    reverse();
    break;
case 7:
    search();
    break;
case 8:
    display();
    break;
default:
    printf("wrong choice");
    break;
    }
}
}

void create_list(){
    int num;
    printf("enter a number:");
    scanf("%d",&num);
struct node *newnode=(struct node *)malloc(sizeof(struct node));
newnode->data=num;
newnode->next=0;
if(head==0){
    head=newnode;
    temp=newnode;
}
else{
    temp->next=newnode;
}
}

void addatbeg(){
 int num;
    printf("enter a number to add at beginning:");
    scanf("%d",&num);
struct node *newnode=(struct node *)malloc(sizeof(struct node));
newnode->data=num;
newnode->next=0;
newnode->next=head;
head=newnode;
}

void delfrbeg(){
temp=head;
printf("the first element deleting: %d",temp->data);
head=head->next;
free(temp);
}

void addbtw(){
    int num,pos;

printf("enter the position at to insert:");
scanf("%d",&pos);
int i=1;
temp=head;
while(i<pos-1){
        if(temp==0){
            printf("nai");
            return;
        }
        temp=temp->next;
        i++;

}

  printf("enter a number to add in between:");
    scanf("%d",&num);
struct node *newnode=(struct node *)malloc(sizeof(struct node));
newnode->data=num;
newnode->next=0;
newnode->next=temp->next;
temp->next=newnode;
}

void delatend(){
    struct node *prevnode;
    head=temp;
while(temp->next!=0){
        prevnode=temp;
    temp=temp->next;
    }
    printf("the last node deleting: %d",temp->data);
prevnode->next=0;
free(temp);
}

void reverse(){
struct node *prevnode,*currentnode,*nextnode;
prevnode=0;
currentnode=nextnode=head;
while(nextnode!=0){
        nextnode=currentnode->next;
        currentnode->next=prevnode;
        prevnode=currentnode;
        currentnode=nextnode;
}
head=prevnode;
printf("\nreversed linked list  is:");
printf("%d\t",nextnode->data);
nextnode=nextnode->next;
}

void search(){
    int val;
    bool found=false;
printf("enter the value to search:");
scanf("%d",&val);
temp=head;
while(temp!=0){
    if(temp->data==val){
        found=true;
    }
    temp=temp->next;
}
     if(found){
     printf("Searched elemnt is present");
     }
     else{
        printf("Searched element is not present");
     }

}

int display(){
if(head==0){
    printf("nil");
}
else{
    temp=head;
    while(temp!=0){
        printf("%d\t",temp->data);
        temp=temp->next;
        count++;
    }
}
return count;
}
