#include<stdio.h>
#include<stdlib.h>
// linear search

//int main()
//{   int num;
//	int arr[10]={1,2,8,3,9,4,5,6,0,7};
//	printf("enter number to search:\n");
//	scanf("%d",&num);
//	int i;
//	for(i=0;i<10;i++)
//	{
//	    if(arr[i]==num)
//		{
//		   printf("element found at index:%d",i);	
//		}
//			
//	}
//	
//
//}

// using while loop


int main()
{   int num;
	int arr[10]={1,2,8,3,9,4,5,6,0,7};
	printf("enter number to search:\n");
	scanf("%d",&num);
	int i;
   while(i<10)
   {
   	  if(arr[i]==num)
   	  {
   	  	printf("value found at index:%d",i);
   	  	exit(0);
	  }
	  
	  i++;
   }
	
	if(i>=10)
	{
		printf("element not found");
		exit(0);
	}

}


