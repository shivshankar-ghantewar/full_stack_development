#include<stdio.h>
int main()
{
    int arr[100]={10,20,30,40,50};
    int size=5;
    int pos;
    int value;

    printf("enter value to add :");
    scanf("%d",&value);

    printf("enter postion to add value :");
    scanf("%d",&pos);

      // Check valid position
    if (pos < 0 || pos > size)
    {
        printf("Invalid position");
        return 0;
    }

    for(int i=size;i>pos;i--)
    {
        arr[i]=arr[i-1];
    }
   arr[pos]=value;
   size++;

   for(int i=0;i<size;i++)
   {
     printf("%d ",arr[i]);
   }
}