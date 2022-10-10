#include<bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    vector<int> shops(n);
    for(int i=0; i<n; i++) cin >> shops[i];

    int q; cin >> q;
    vector<int> coins(q);
    for(int i=0; i<q; i++) cin >> coins[i];

    sort(shops.begin(), shops.end());
    vector<int> ans;

    for(int i=0; i<q; i++){
        int x = upper_bound(shops.begin(), shops.end(), coins[i]) - shops.begin();
        ans.push_back(x);
    }

    for(int num: ans) cout << num << endl;
    // vector<int> teamA = {1,3,2,6};
    // vector<int> teamB = {3,5};
    // vector<int> ans;
    // sort(teamA.begin(), teamA.end());

    // for(int i=0; i<teamB.size(); i++){
    //     int it = upper_bound(teamA.begin(), teamA.end(), teamB[i]) - teamA.begin();
    //     cout << it << " ";
    //     ans.push_back(it);
    // }
    // return ans;

    

}