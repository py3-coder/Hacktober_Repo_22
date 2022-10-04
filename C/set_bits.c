#include<stdio.h>

int main(){
    int num, temp, count = 0;
    printf("Enter any number to find number of setbits it contains: ");
    scanf("%d", &num);
    temp = num;
    while (num>0){
        count += (num&1);
        num >>= 1;
    }
    printf("\n%d has %d setbits.\n", temp, count);
    return 0;
}