#include <bits/stdc++.h>

using namespace std;

void shift(int arr[], int n)
{
    int count=0;
 
    for(int i=0;i<n;i++)
    {
        if(arr[i]!=0)
        {
            swap(arr[i],arr[count]);
            count++;
            }
        
    
        
    }
    

    
    
    cout<<"------------------"<<endl;
    for(int i =0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
}

int main()
{
    int n;
    cout<<"Enter the lenght of the array"<<endl;
    cin>>n;
    int arr[n];
    cout<<"Enter the values in the array"<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    shift(arr,n);
    return 0;
}
