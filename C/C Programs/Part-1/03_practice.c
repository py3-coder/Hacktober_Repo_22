#include<stdio.h>

int main(){
    float celsius = 37, far;
    far = (celsius * 9 / 5) + 32;
    printf("The value of this celsius temperature in Fahrenheit is %f", far);
    return 0;
}