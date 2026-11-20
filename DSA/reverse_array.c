
#include<stdio.h>

int main()
{
    int arr[] = {4, 2, 7, 1, 9, 5};
    int size=sizeof(arr)/sizeof(arr[0]);

    for(int i=size-1;i>=0;i--)
    {
        printf("%d ",arr[i]);
    }
}