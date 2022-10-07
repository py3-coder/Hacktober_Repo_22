// it gives no output because 
/* The decimal fraction 1.1 cannot be represented exactly using binary floating-point numbers (just like fraction 1/3 cannot be represented exactly using decimal floating-point numbers).

When you attempt to put 1.1 in type double, what you really store is 1.100000000000000088817841970012523233890533447265625

When you attempt to put 1.1 in type float, what you really store is 1.10000002384185791015625

Those values are not equal, so "x == 1.1" is false!

To make your program work, either use double

double x=1.1; while (x==1.1) ... 
or use float:

float x=1.1f; while (x==1.1f) ... 
but don’t mix the types */

#include<stdio.h>

int main(){
	float x = 0.125;
	while(x== 0.125){
		printf("%f\n",x);
		x=x-0.1;    
	}
	return 0;
}
