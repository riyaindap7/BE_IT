#include <stdio.h>
#include <stdlib.h>

void selectionSort(int arr[], int n) {
for (int i = 0; i < n - 1; i++) {
int minIndex = i;
for (int j = i + 1; j < n; j++) {
if (arr[j] < arr[minIndex]) {
minIndex = j;
}
}
int temp = arr[i];
arr[i] = arr[minIndex];
arr[minIndex] = temp;
}
}

void merge(int arr[], int left[], int right[], int leftSize, int rightSize) {
int i = 0, j = 0, k = 0;

while (i < leftSize && j < rightSize) {
if (left[i] < right[j]) {
arr[k++] = left[i++];
} else {
arr[k++] = right[j++];
}
}

while (i < leftSize) {
arr[k++] = left[i++];
}

while (j < rightSize) {
arr[k++] = right[j++];
}
}

void mergeSort(int arr[], int n) {
if (n > 1) {
int mid = n / 2;
int *left = (int *)malloc(mid * sizeof(int));
int *right = (int *)malloc((n - mid) * sizeof(int));

for (int i = 0; i < mid; i++) {
left[i] = arr[i];
}

for (int i = mid; i < n; i++) {
right[i - mid] = arr[i];
}

mergeSort(left, mid);
mergeSort(right, n - mid);
merge(arr, left, right, mid, n - mid);

free(left);

free(right);
}
}

int main() {
int choice;
int n;

printf("Enter the number of elements: ");
scanf("%d", &n);

int arr[n];

printf("Enter the elements: ");
for (int i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}

while (1) {
printf("\nMenu:\n");
printf("1. Selection Sort\n");
printf("2. Merge Sort\n");
printf("3. Quit\n");
printf("Enter your choice: ");
scanf("%d", &choice);

switch (choice) {
case 1:
selectionSort(arr, n);

printf("Sorted using Selection Sort: ");
break;
case 2:
mergeSort(arr, n);
printf("Sorted using Merge Sort: ");
break;
case 3:
printf("Exiting the program.\n");
exit(0);
default:
printf("Invalid choice. Please choose 1, 2, or 3.\n");
continue;
}

for (int i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
return 0;
}
