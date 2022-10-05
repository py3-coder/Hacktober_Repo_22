//Importing the libraries
#include <iostream>
using namespace std;

//Function for Binary Search
int BinarySearch (int arr[], int size, int element)
{   int start=0, end=size-1;
    int mid=(size+end)/2;
    while(start<=end)
    {
        if(arr[mid] == element)
        {
           return mid;
        }
        else if(arr[mid]>element)
        {
           end=mid-1;
        }
        else
        {
           start=mid+1;
        }
        mid=(start+end)/2;
    
    }
    return -1;
    
}

int main()
{   int size,element;
    cout<<"Enter the size of an array:";
    cin>>size;
    int arr[size];
    cout<< "Enter the elements of array in increasing order:";
    
    for(int i=0;i<size;i++)
    {
       cin>>arr[i];
    }
    cout<< "Enter the element:";
    cin>> element;
    int found = BinarySearch (arr,size, element);
    if(found == -1)
    {
       cout<< element <<" is not found in the array\n";
    
    }
    else
    {
       cout << element <<" is found in the array at position "<< found+1 << endl;
    }
    return 0;
}
