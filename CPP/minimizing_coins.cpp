#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define ull unsigned long long int
#define ld long double
#define mod 1000000007

ll find(vector<ll>& u,ll s,ll n)
{
  sort(u.begin(),u.end());
  vector<ll> dp(s+1,0);
  for(int i=1;i<=s;i++)
  {
    dp[i]=INT_MAX;
  }
  for(int i=1;i<=n;i++)
  {
    for(int j=1;j<=s;j++)
    {
      if(u[i-1]<=j) dp[j]=min(dp[j],dp[j-u[i-1]]+1);
    }
  }
  ll res=dp[s]>=INT_MAX?-1:dp[s];
  return res;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  ll n,x;
  cin>>n>>x;
  vector<ll> v(n);
  for(int i=0;i<n;i++)
  {
    cin>>v[i];
  }
  cout<<find(v,x,n)<<endl;
  return 0;
}
