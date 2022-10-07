// C++ program to illustrate
// next_permutation example

// this header file contains next_permutation function
#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
	int n;
  cin>>n;
  int arr[n];
  for(int i=0;i<n;i++){
    cin>>arr[i];
  }
next_permutation(arr,arr+n);
for(int i=0;i<n;i++){
  cout<<arr[i]<<" ";
}cout<<endl;
	return 0;
}
