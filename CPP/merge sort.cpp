# include <iostream>
# include <math.h>
using namespace std;
int gcd(int a, int b) {

    if(a==0)
    return b;

    if(b==0)
    return a;

    while(a != b) {

        if(a>b)
        {
            a = a-b;
        }
        else{
            b = b-a;
        }
    }
    return a;
}

/*void sortArray(int *arr,int n)
{
  if((n==0)||(n==1))
  {
    return;
  }
  for(int i=0;i<n-1;i++)
  {
    if(arr[i]>arr[i+1])
    {
      swap(arr[i],arr[i+1]);
    }
  }
  sortArray(arr,n-1);
}
*/
int main()
{
  /*int arr[6]={9,4,5,2,10,2};
  sortArray(arr,5);
  for(int i=0;i<5;i++)
  {
 cout<< arr[i]<<" "<<endl;
  }
  */
  int a,b;
    cout << "Enter the Values of a and b" << endl;
    cin >> a >> b;

    int ans = gcd(a,b);

    cout << " The GCD of " << a << " & " << b << " is: " << ans << endl;


}