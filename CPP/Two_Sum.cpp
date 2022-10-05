//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> ans(2);
        for(int i = 0; i < nums.size(); i++)
            map[nums[i]] = i;
        for(int x = 0; x < nums.size(); x++){
            int val = target - nums[x];
            auto itr = map.find(val);
            if(itr != map.end() && x!= itr->second){
                ans[0] = x;
                ans[1] = itr->second;
                break;
            }          
        }
        return ans;
    }
};

