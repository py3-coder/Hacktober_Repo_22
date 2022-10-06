#include<stdio.h>

int main(){
    int physics, chemistry, maths;
    float total;
    printf("Enter Physics Marks\n");
    scanf("%d", &physics);

    printf("Enter Chemistry Marks\n");
    scanf("%d", &chemistry);

    printf("Enter Maths Marks\n");
    scanf("%d", &maths);
    total = (physics + maths + chemistry)/3;
    if((total<40) || physics<33 || maths<33 || chemistry<33){
        printf("Your total percentage is %d and you are fail\n", total);
    }
    else{
        printf("Your total percentage is %d and you are pass\n", total);
    }
    return 0;
}