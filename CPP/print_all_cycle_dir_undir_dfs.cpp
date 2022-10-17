// Printing all Cycles in a Graph
// This code is for both directed(default) ans undirected graph
// Input - Directed Graph: n = 10, m = 12
// 1 
// 10 12
// 1 2 
// 2 3
// 2 5
// 2 8
// 2 10
// 3 4
// 4 2
// 5 6
// 6 7
// 7 2
// 8 9
// 9 10

#include<bits/stdc++.h>
using namespace std;
#define endl '\n'
int n, m;

vector<vector<int>> g;
vector<int> col;
vector<int> parent;
vector<vector<int>> sol;
bool is_cycle = 0;

void dfs(int node, int par){
    col[node] = 2;
    parent[node] = par;
    for(auto x : g[node]){
        if(col[x] == 1){
            dfs(x, node);
        }
        else if(col[x]==2){
            vector<int> cursol;
            int temp = node;
            while(temp!=x){
                cursol.push_back(temp);
                temp = parent[temp]; 
            }
            cursol.push_back(x);
            reverse(cursol.begin(), cursol.end());
            sol.push_back(cursol);
            cursol.clear();
        }
        else if(col[x]==3){

        }
    }
    col[node] = 3;
}

void solve(){
    cin >> n >> m;
    g.clear();
    sol.clear();
    g.resize(n+1);
    parent.resize(n+1);
    col.assign(n+1 , 1);
    
    int x, y;
    for(int i = 0; i < m; i++){
        cin >> x >> y;
        g[x].push_back(y);
    }

    for(int i = 1; i <= n; i++){
        if(col[i]==1){
            dfs(i, 0);
        }
    }

    cout<<"Cycle hai graph me :D"<<endl;
    int i = 1;
    for(auto s : sol){
        cout<< "Cycle "<<i<<" : ";
        for(auto v : s){
            cout << v <<" ";
        }
        cout<<endl;
        i++;
    }
    cout << endl;
}
signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    int _t;cin>>_t;while(_t--)
    solve();
}