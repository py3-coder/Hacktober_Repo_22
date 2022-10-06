/ C++ program for Pascal’s Triangle
// A O(n^2) time and O(1) extra space 
// function for Pascal's Triangle
#include <bits/stdc++.h>
  
using namespace std;
void printPascal(int n)
{
      
for (int line = 1; line <= n; line++)
{
    int C = 1; // used to represent C(line, i)
    for (int i = 1; i <= line; i++) 
    {
          
        // The first value in a line is always 1
        cout<< C<<" "; 
        C = C * (line - i) / i; 
    }
    cout<<"\n";
}
}
  
// Driver code
int main()
{
    int n = 5;
    printPascal(n);
    return 0;
}
