// Problem Statement - Given a number of stairs(N).Calculate number of
//                     distinct ways to climb from 0th step to Nth step.

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n=5;    //No. of stairs  
    vector<int> dp(n+1,-1); //DP vector to store no. of ways and initializing with -1

    //Storing initial values of DP vector
    dp[0] = 1;
    dp[1] = 1;
    
    for(int i = 2; i <= n; i++)
    {
        dp[i] = dp[i - 1] + dp[i - 2]; //Tabulation
    }
    cout << dp[n];   
}

//Time Complexity - O(n)
//Space Complexity - O(n)