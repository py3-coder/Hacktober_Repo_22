#include<bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin>>n;


    int digit;
    int ans = 0;
    int i = 0;
    while (n != 0)
    {
        digit = n%10;
        if (digit == 1)
        {
            /* code */
            ans = ans+pow(2,i);
        }
        n = n/10;
        i++;
        

    }
    cout<<ans<<endl;
    
    return 0;
}   
