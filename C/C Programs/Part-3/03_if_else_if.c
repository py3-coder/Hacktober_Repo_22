#include<stdio.h>

int main(){
    int num;

    printf("Enter your number\n");
    scanf("%d", &num);

    if(num==1){
        printf("Your number is 1\n");
    }
    else if (num == 2)
    {
        printf("Your number is 2\n");
    }
    else if (num == 3)
    {
        printf("Your number is 3\n");
    }
    else{
        printf("Its not 1, 2 or 3!\n");
    }
     

    return 0;
}