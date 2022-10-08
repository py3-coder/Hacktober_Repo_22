#include<stdio.h>
void goodMorning();
void goodAfternoon();
void goodNight();

int main(){
    goodMorning();
    return 0;
}

void goodMorning(){
    printf("Good Morning Harry\n");
    goodAfternoon();
}

void goodAfternoon(){
    printf("Good Afternoon Harry\n");
    goodNight();
}

void goodNight(){
    printf("Good Night Harry\n");
}