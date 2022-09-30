/*
46. Permutations
Medium
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]
 
Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
*/
//CODE 1: 
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subres = new ArrayList<>();
        Solve(nums,subres,res);
        return res;
    }
    public static void Solve(int nums[],List<Integer> subres,List<List<Integer>> res){
        if(subres.size()==nums.length){
            res.add(new ArrayList<Integer>(subres));
            return;
        }else{
            for(int i=0;i<nums.length;i++){
                if(subres.contains(nums[i])) continue;
                subres.add(nums[i]);
                Solve(nums,subres,res);
                subres.remove(subres.size()-1);
            }
        }   
    } 
}
// CODE 2:
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        
        Solve(nums,0,res);
        return res;
    }
    public static void Solve(int nums[],int idx,List<List<Integer>> res){
        if(idx==nums.length){
            List<Integer> nn = new ArrayList<>();
            for(int i=0;i<nums.length;i++){
                nn.add(nums[i]);
            }
            res.add(new ArrayList<Integer>(nn));
            return;
        }else{
            for(int i=idx;i<nums.length;i++){
                swap(i,idx,nums);
                Solve(nums,idx+1,res);
                swap(i,idx,nums);
            }
        }   
    }
    public static void swap(int i,int j,int[] nums){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp; 
    }
}
