#include<stdio.h>

void bubblesort(int arr[],int n)
{
  int temp;
  for(int i=0;i<n-1;i++)
  {
  	for(int j=0;j<n-i-1;j++)
  	{
  		if(arr[j]>arr[j+1])
  		{
  			temp=arr[j];
  			arr[j]=arr[j+1];
  			arr[j+1]=temp;
		  }
	  }
  }
}


int main()
{
	int array[]={2,5,4,9,7,1};
	int size=sizeof(array)/sizeof(array[0]);
	bubblesort(array,size);
	
	printf("sorted array:");
	for(int i=0;i<size;i++)
	{
		printf("%d",array[i]);
	}
	
	return 0;
}
