#include<stdio.h>

int binsearch(int a[], int elem, int start,int end){
	int mid = start + end / 2;
	if(elem == a[mid])
		return mid;
	else if(start > end)
		return -1;
	else if(a[mid] > elem)
		return binsearch(a,elem,start,mid);
	else
		return binsearch(a,elem,mid,end);
}

int main(void){
	int i,a[5],elem, t;
	printf("Enter elements for array\n");
	for(i=0;i<5;i++){
		printf("%d: ",i);
		scanf("%d",&a[i]);
	}
	printf("Enter element to search: ");
	scanf("%d",&elem);
	t= binsearch(a,elem,0,5);
	if(t==-1){
		printf("Element not found\n");
	}else
		printf("The element was found at position: %d\n", t);
	return 0;
}
