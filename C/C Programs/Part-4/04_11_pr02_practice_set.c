#include<stdio.h>

int main(){
    printf("****Multiplication table of 10****\n\n");
    for(int i=10;i;i--){
        printf("10 X %d = %d\n", i, 10*i);
    }
    return 0;
}