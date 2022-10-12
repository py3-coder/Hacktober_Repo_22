#include<stdio.h>

int add();
int sub();
int mult();
int div();
int a,b,res;
int main()
{
	int c,d;
	do
	{
		printf("\n1.Add 2.Subtract 3.Multiply 4.Division 5.exit\n");
		printf("enter your choice");
		scanf("%d",&c);
		switch(c)
		{
			case 1:d=add();
			printf("result is %d",d);
			break;
			case 2:d=sub();
			printf("result is %d",d);
			break;
			case 3:d=mult();
			printf("result is %d",d);
			break;
			case 4:d=div();
			printf("result is %d",d);
			break;
		}
    }
	while(c!=5);
    return 0;
}
int add()
{
	printf("Enter 2 numbers:");
	scanf("%d%d",&a,&b);
	res=a+b;
	return res;
}

int sub()
{
	printf("Enter 2 numbers:");
	scanf("%d%d",&a,&b);
	res=a-b;
	return res;
}

int mult()
{
	printf("Enter 2 numbers:");
	scanf("%d%d",&a,&b);
	res=a*b;
	return res;
}

int div()
{
	printf("Enter 2 numbers:");
	scanf("%d%d",&a,&b);
	res=a/b;
	return res;
} 
 
 
 
 
