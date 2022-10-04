#include<bits/stdc++.h>
using namespace std;

unordered_map<char,int>symbol={ {'[',-1},{'(',-2},{'{',-3},{']',1},{')',2},{'}',3}};
void solve()
{
        string s;
        cin >> s;
        stack<char>st;
        for(auto bracket : s)
        {
                if(symbol[bracket]<0)
                {
                        st.push(bracket);
                }
                else
                {
                        if(st.empty())
                        {
                                cout << "NO\n";
                                return;
                        }
                        char top=st.top();
                        st.pop();
                        if(symbol[top]+symbol[bracket]!=0)
                        {
                                cout << "NO\n";
                                return;
                        }
                }
        }
        if(st.empty())
        {
                cout << "YES\n";
                return;
        }
        cout << "NO\n";
        return;
        
}

int main()
{
        int t;
        cin >> t;
        while(t--)
        {
                solve();
        }
}

