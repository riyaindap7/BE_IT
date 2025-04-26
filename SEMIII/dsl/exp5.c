//code for directed graph
/*#include<stdio.h>

int main()
{
    int i,j;
    int arr[3][3];
    printf("enter elements\n");
    for (i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            scanf("%d\n",&arr[i][j]);
        }
    }
      for (i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            printf("%d\t",arr[i][j]);
        }
        printf("\n");
    }
}*/

#include<stdio.h>
#include<stdlib.h>
#define MAX 20
int adj[MAX][MAX];
int n;
void create_graph();
void display();
void insert_edge(char u,char v);
void del_edge(char u, char v);
void insert_node();
void delete_node(char u);

int main()
{

    int choice;
    int node,origin,dest;
    create_graph();
    while(1)
    {
        printf("1.Insert a node\n");
        printf("2.insert a edge\n");
        printf("3.delete a node\n");
        printf("4.delete a edge\n");
        printf("5.display\n");
        printf("6.exit\n");
        printf("enter your choice:");
        scanf("%d",&choice);

        switch(choice)
        {
        case 1:
            insert_node();
            break;
        case 2:
            printf("enter an edge to be inserted:");
            fflush(stdin);
            scanf("%d %d",&origin,&dest);
            //insert_edge(origin,dest);
            break;
        case 3:
            printf("enter a node to be deleted:");
            fflush(stdin);
            scanf("%d",&node);
            delete_node(node);
            break;
        case 4:
            printf("enter the edge to be deleted:");
            fflush(stdin);
            scanf("%d %d",&origin,&dest);
            //del_edge(origin,dest);
        case 5:
            display();
            break;
        case 6:
            //exit(1);
        default:
            printf("wrong choice\n");
            break;

        }
    }

}

void create_graph()
{
    int i,max_edges,origin,dest;
    printf("enter the number of node:");
    scanf("%d",&n);
    max_edges=n*(n-1);
    for(i=1;1<=max_edges;i++)
    {
        printf("enter edge %d( 0 0) to quit:",i);
        scanf("%d %d",&origin,& dest);
        if((origin==0)&&(dest==0))
            break;
        if(origin>n|| dest>n||origin<=0||dest<=0)
        {
            printf("Invalid edge\n");
            i--;
        }
        else
        {
            adj[origin][dest]=1;
        }
    }
}

void display()
{
    int i,j;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        {
            printf("%4d",adj[i][j]);

        } printf("\n");
    }
}

void insert_node()
{
    int i;
    n++;
    printf("the inserted node is %d\n",n);
    for(i=1;i<=n;i++)
    {
        adj[i][n]=0;
        adj[n][i]=0;

    }
}

void delete_node(char u)
{
    int i, j;
    if(n==0)
    {
        printf("graph is empty\n");
        return;
    }
    for(i=u;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        {
            adj[j][i]=adj[j][i+1];
            adj[i][j]=adj[i+1][j];
        }
    }n--;
}
void insert_edge(char u,char v)
{
	if(u > n)
	{
		printf("Source node does not exist\n");
		return;
	}
	if(v > n)
	{
		printf("Destination node does not exist\n");
		return;
	}
	adj[u][v]=1;
}/*End of insert_edge()*/

void del_edge(char u,char v)
{
     if(u>n || v>n || adj[u][v]==0)
     {
	printf("This edge does not exist\n");
	return;
     }
     adj[u][v]=0;
}/*End of del_edge()*/
