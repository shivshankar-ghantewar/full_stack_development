
// space complexity

#include<stdio.h>

void square(int num)
{
	printf("size of num var:%d\n",sizeof(num));
	printf("size of data type of int:%d\n",sizeof(int)); //4 byte
	printf("size of data type of float:%d\n",sizeof(float)); // 4 byte
	printf("size of data type of double:%d\n",sizeof(double)); // 8 byte

	printf("square:%d",num*num);

}


int main(){
	double num=5;
	square (num);
	return 0;
}
