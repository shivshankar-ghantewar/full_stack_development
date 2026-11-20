
#include<stdio.h>

int main()
{
 int arr[]={4,8,6,3,2,1};
 int size=sizeof(arr)/sizeof(arr[0]);
 int largest=0;

 for(int i=0;i<size;i++)
 {
   if(arr[i]>largest)
   {
     largest=arr[i];
   }
 }

 printf("the largest number is:%d",largest);

}