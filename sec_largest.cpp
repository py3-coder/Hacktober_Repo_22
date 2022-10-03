#include <bits/stdc++.h>

using namespace std;



int sec_largest(int arr[],int n)
{
   int sec_max=-1;
   int max=0;
   
   for(int i=1;i<n;i++)
   {
       if(arr[i]>arr[max])
       {
           sec_max=max;
           max=i;
       }
       
       else if(arr[i]!=arr[max])    
       {
           if(sec_max==-1 || arr[i]>sec_max)
           {
               sec_max=i;
           }
       }
       
   }
    return sec_max;
}


int main()
{
    int n;
    cout<<"Enter the length of the array"<<endl;
    cin>>n;
    int arr[n];
    cout<<"Enter the elements in the array"<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    
    cout<<"second largest no. is at: "<<sec_largest(arr,n);
    
    return 0;
}
