

#include <iostream>

using namespace std;
bool linearsearch(int arr[],int n,int x)
{
    if(n==0)
    return false;
    if(arr[0]==x)
    return true;
    else
    return linearsearch(arr+1,n-1,x);
}


int main()
{
    int arr[]={1,2,7,4,5};
    cout<<linearsearch(arr,5,0);

    return 0;
}

