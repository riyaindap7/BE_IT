#include <stdio.h>
#include <malloc.h>

struct node
{
    int info;
    struct node *lchild;
    struct node *rchild;
}*root;

void insert(int);
void del(int);
//void inorder(struct node*);
//void preorder(struct node*);
//void postorder(struct node*);
void display(struct node*, int);
//void exit();
void find(int, struct node **, struct node **);
//void case_a(struct node *, struct node *);
//void case_b(struct node *, struct node *);
//void case_c(struct node *, struct node *);

int main()
{
    int choice, num;
    root = NULL;

    while(1)
    {
        printf("1. Insert\n2. Delete\n3. Inorder\n4. Preorder\n5. Postorder\n6. Display\n7. Exit\n Enter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter the number to be inserted: ");
                scanf("%d", &num);
                insert(num);
                break;
            case 2:
                printf("Enter number to be deleted: ");
                scanf("%d", &num);
                del(num);
                break;
            case 3:
                //inorder(root);
                break;
            case 4:
                //preorder(root);
                break;
            case 5:
                //postorder(root);
            case 6:
                display(root, 1);
                break;
            case 7:
                //exit();
            default:
                printf("Wrong choice\n");
        }
    }
    return 0;
}

void find(int item, struct node **par, struct node **loc)
{
    struct node *ptr, *ptrsave;

    if (root == NULL)
    {
        *loc = NULL;
        *par = NULL;
        return;
    }
    if(item == root -> info)
    {
        *loc = root;
        *par = NULL;
        return;
    }
    if(item < root -> info)
        ptr = root -> lchild;
    else
        ptr = root -> rchild;
    ptrsave = root;

    while(ptr !=NULL)
    {
        if(item == ptr -> info)
        {
            *loc = ptr;
            *par = ptrsave;
            return;
        }
        ptrsave = ptr;
        if(item < ptr -> info)
            ptr = ptr -> lchild;
        else
            ptr = ptr -> rchild;
    }
    *loc = NULL;
    *par = ptrsave;
}

void insert(int item)
{
    struct node *tmp, *parent, *location;
    find(item, &parent, &location);
    if(location != NULL)
    {
        printf("Item already exist\n");
        return;
    }
    tmp = (struct node *)malloc(sizeof(struct node));
    tmp -> info = item;
    tmp -> lchild = NULL;
    tmp -> rchild = NULL;

    if(parent == NULL)
        root = tmp;
    else
        if(item < parent -> info)
            parent -> lchild = tmp;
        else
            parent -> rchild = tmp;
}

void del(int item)
{
    struct node *parent, *location;
}

void display(struct node *ptr, int level)
{
    int i;
    if(ptr != NULL)
    {
        display(ptr -> rchild, level + 1);
        printf("\n");
        for(i=0; i<level; i++)
            printf("   ");
        printf("%d", ptr -> info);
        display(ptr -> lchild, level + 1);
        printf("\n");
    }
}
