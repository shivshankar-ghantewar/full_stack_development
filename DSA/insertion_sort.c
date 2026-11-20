#include<stdio.h>

void insertionsort(int arr[],int size)
{
    int i,j,key;
    for(i=1;i<size;i++)
    {
        key=arr[i];

        for(j=i-1;j>=0 && arr[j]>key;j--)
        {
            arr[j+1]=arr[j];
        }

        arr[j+1]=key;
    }
}

void display(int arr[],int size)
{
    for(int i=0;i<size;i++)
    {
        printf(" %d",arr[i]);
    }
}




int main()
{
  int arr[]={6,7,3,4,1};
  int size=sizeof(arr)/sizeof(arr[0]);

  printf("unsorted array:");
  display(arr,size);

  insertionsort(arr,size);

  printf("\n  sorted array:");
  display(arr,size);
}