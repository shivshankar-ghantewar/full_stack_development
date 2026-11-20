#include<stdio.h>

int main()
{
    int arr[]={8,5,4,7,9};
    int size=sizeof(arr)/sizeof(arr[0]);
    int smallest=arr[0];
    
    
    for(int i=0;i<size;i++)
    {  
    
        if(arr[i]<smallest)
        {  
            smallest=arr[i];
        }
    }

    printf("smallest number:%d",smallest);
}