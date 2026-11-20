#include<stdio.h>
#include<stdlib.h>

int main()
{
    int arr[5]={10,20,30,40,50};
    int size=sizeof(arr)/sizeof(arr[0]);
    int upper=size-1,lower=0,mid,f=0,element;

    printf("enter targeted number:\n");
    scanf("%d",&element);

    while(lower<=upper)
    {
        mid=(lower+upper)/2;

        if(arr[mid]==element)
        {
             f=1;
             break;

        }

        if(arr[mid]<element)
        {
            lower=mid+1;
        }
        else
        {
            upper=mid-1;
        }
 
    }

    if(f==1)
        {
            printf("element found at position:%d",mid+1);
        }
        else{
            printf("element not found");
        }
  
}