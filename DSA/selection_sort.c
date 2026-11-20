
#include<stdio.h>

int main()
{
  int arr[]={3,4,1,2,5,9,7,8,6};
  int size=9;
  int temp,min;

  for(int i=0;i<size-1;i++)
  {
    min=i;
    for(int j=i+1;j<size;j++)
    {
    if(arr[j]<arr[min])
    {
          min=j;
    }
    }

    // swap
    temp=arr[min];
    arr[min]=arr[i];
    arr[i]=temp;
  }

  for(int i=0;i<size;i++)
  {
    printf("%d ",arr[i]);
  }
}