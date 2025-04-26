#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#define MAX 10

int arr[MAX];
void sorting(int arr[],int n);

int main(){
    int n,i;
    printf("enter number of elements to sort:");
    scanf("%d",&n);
printf("enter the elements to be sorted:");
for(i=0;i<n;i++){
    scanf("%d\n",&arr[i]);
}
printf("\nunsorted array is:");
for( i=0;i<=n-1;i++){
    printf("%d ",arr[i]);
}

sorting(arr,n);
printf("\nsorted array is:");
for( i=0;i<=n-1;i++){
    printf("%d ",arr[i]);

}
}


void sorting(int arr[],int n){
    int temp,j;
for(int k=1;k<n;k++){
    temp=arr[k];
    j=k-1;
   while(temp<arr[j] && j>=0){

            arr[j+1]=arr[j];
            j--;
   }
        j=j+1;
        arr[j]=temp;
    }
}

