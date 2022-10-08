

#include <iostream>

using namespace std;
bool sort(int arr[],int n)
{
    if(n==0)
    return true;
    if(arr[0]>arr[1])
    return false;
    else
    return sort(arr+1,n-1);
}


int main()
{
    int arr[]={1,2,6,4,5};
    cout<<sort(arr,5);

    return 0;
}

