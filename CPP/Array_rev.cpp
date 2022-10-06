#include <iostream>
using namespace std;

int main()
{
    int arr[100], rev[100], size, i;
    
    cout<<"Enter the size of an array\n";
    cin>>size;

    cout<<"Enter "<<size<<" numbers: \n";

    for ( i = 0; i < size; i++)
    {
        cin>>arr[i];
    }

    for ( i = 0; i < size; i++)
    {
        rev[i]=arr[size-i-1];
    }

    cout<<"Reversed array\n";

    for ( i = 0; i < size; i++)
    {
        cout<<rev[i]<<" ";
    }
    
    return 5;
}
