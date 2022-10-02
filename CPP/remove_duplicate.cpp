//To remove the duplicate elements from a sorted array without using another array

# include<bits/stdc++.h>
using namespace std;

int remDups(int arr[], int n)
{
    //int temp[n];
    //temp[0]=arr[0];
    int res=1;
    
    for(int i=1;i<n;i++)
    {
        if(arr[res-1]!=arr[i])
        {
            arr[res]=arr[i];
            res++;
        }
    }
    
    
    return res;
}

int main()
{
    int n;
    cout<<"Enter the size of the array";
    cin>>n;
    int arr[n];
    cout<<"Enter the elements in the array";
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    
    cout<<remDups(arr,n);
}
