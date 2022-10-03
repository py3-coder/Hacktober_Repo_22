
#include <bits/stdc++.h>

using namespace std;

int search(int arr[], int n ,int key)
{
    for(int i=0;i<n;i++)
    {
        if (arr[i]==key)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    int n,key;
    cout<<"Enter the length of the array"<<endl;
    cin>>n;
    int arr[n];
    cout<<"Enter the elements in the array"<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    
    cout<<"Enter a number to search"<<endl;
    cin>>key;
    
    cout<<"index of the elemnt is: "<< search(arr,n,key);

    return 0;
}
