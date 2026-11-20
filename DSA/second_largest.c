
#include<stdio.h>
int main()
{
    int arr[]={4,5,2,3,7,8,1};
    int size=sizeof(arr)/sizeof(arr[0]);
    int largest=0,second_largest=0;

    // find largest
    for(int i=0;i<size;i++)
    {
        if(largest<arr[i])
        {
            second_largest=largest;
            largest=arr[i];
        }

    }

    // find second_largest
     for(int i=0;i<size;i++)
    {
        if(largest>arr[i]  && arr[i]>second_largest)
        {
        
            second_largest=arr[i];
        }

    }

    printf("largest number:%d \n",largest);
    printf("second_largest number: %d",second_largest);
}