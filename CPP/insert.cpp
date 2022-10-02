#include <bits/stdc++.h>

using namespace std;

void insert(int arr[], int n ,int key, int pos)
{
    int index = pos-1;
    for(int i=n;i>=index;i--)
    {
        arr[i+1]=arr[i];
    }
    arr[index]=key;
    
    for(int i=0;i<n+1;i++)
    {
        cout<<arr[i]<<" ";
    }
    
    // for()
    // return arr;
}

// void print_arr(int arr[],int n)
// {
//     for(int i=0;i<n+1;i++)
//     {
//         cout<<arr[i]<<" ";
//     }
    
// }

int main()
{
    int n,key,pos;
    cout<<"Enter the length of the array"<<endl;
    cin>>n;
    int arr[n+1];
    cout<<"Enter the elements in the array"<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    

    cout<<"Enter a number to insert"<<endl;
    cin>>key;
    
    cout<<"Enter the position at which key should be inserted"<<endl;
    cin>>pos;
    
    //cout<<"index of the elemnt is: "<< 
    insert(arr,n, key,pos);
    
    //print_arr(arr,n);
    return 0;
}
