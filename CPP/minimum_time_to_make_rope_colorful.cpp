
//Leetcode daily challenge problem
//Link: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


class Solution {
public:         //O(n) solution
    int minCost(string colors, vector<int>& time) {
        int n = time.size();
        int ans = 0;
        //to maintain prev color
        int prev = 0;

        for(int cur=1; cur<n; cur++){
            //if cur and prev colors are same update and delete min ones
            if(colors[prev] == colors[cur]){
                if(time[prev] < time[cur]){
                    ans += time[prev];
                    prev = cur;
                }else{
                    ans += time[cur];
                }
            }else{
                prev = cur;
            }
        }
        return ans;
    }
};