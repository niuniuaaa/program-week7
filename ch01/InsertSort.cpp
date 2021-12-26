#include<stdlib.h>
#include<stdio.h>
void insertionsortS(int a[],int size)
{
    for (int j = 1; j < size; j++)
    {
        int i = j - 1;
        int key = a[j];
        while (i >= 0 && a[i] > key)
        {
            a[i + 1] = a[i];
            i--;
        }
        a[i + 1] = key;
    }
}
//循环不变式 
void insertionsort(int a[], int size) {
    int i = size - 2;
    while (i > -1)
    {
        int j = i + 1;
        int key = a[i];
        while (j < size&&a[j]>key)
        {
            a[j - 1] = a[j];
            j++;
        }
        a[j - 1] = key;
        i--;
    }
}
int main()
{
	int a[6]={2,4,3,10,7,4};
	insertionsort(a,6);
	insertionsortS(a,6);
	for(int i=0;i<6;i++)
	{
		printf("%d ",a[i]);
	}
	return  0;
 } 
