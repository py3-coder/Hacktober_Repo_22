//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
    public:
    
    void solve(int index , string S , set<string>&st){
        
        
        if(index == S.size()){
            st.insert(S);
            return ;
        }
        
        for(int j=index;j<S.size();j++){
            swap(S[index] , S[j]);
            
            solve(index+1 , S , st);
            
            swap(S[index] , S[j]);
        }
    }
    //Complete this function
    
    vector<string> permutation(string S)
    {
        //Your code here
        set<string> st;
        
        solve(0,S,st);
        
        vector<string>ans(st.begin(),st.end());
        
        return ans;
    }
};

//{ Driver Code Starts.

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		string S;
		cin>>S;
		Solution ob;
		vector<string> vec = ob.permutation(S);
		for(string s : vec){
		    cout<<s<<" ";
		}
		cout<<endl;
	
	}
	return 0;
}
// } Driver Code Ends
