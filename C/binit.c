#include<stdio.h>

int main(void){
	int i,a[5],elem, t, start=0, end=5, mid;
	printf("Enter elements for array\n");
	for(i=0;i<5;i++){
		printf("%d: ",i);
		scanf("%d",&a[i]);
	}
	printf("Enter element to search: ");
	scanf("%d",&elem);
	while(start<=end){
		mid=start+end/2;
		if(elem==a[mid]){
			printf("Element found at position: %d\n", mid);
			return 0;
		}else if(elem>a[mid])
			start=mid;
		else
			end=mid;
	}
	printf("The element was not found\n");
	return 0;
}
