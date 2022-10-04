#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int a,b;
    cout<<"Enter two numbers:";
    cin>>a>>b;
    cout<<"Greatest Common Divisor of "<<a<<" and "<<b<<" is:"<<__gcd(a,b);
    return 0;
}