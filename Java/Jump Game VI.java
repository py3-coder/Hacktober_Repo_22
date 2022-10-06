/******************************************************************************
Leet Code :1696. Jump Game VI
Link : https://leetcode.com/problems/jump-game-vi/
*******************************************************************************/

class Solution {
    private PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (b[0] - a[0]));

    public int maxResult(int[] nums, int k) {
        if (nums.length == 0)
            return 0;

        pq.add(new int[] { nums[0], 0 });

        int ans = nums[0];

        for (int i = 1; i < nums.length; i++) {
            while(i - pq.peek()[1] > k)
                pq.remove();

            ans = pq.peek()[0]+nums[i];
            pq.add(new int[] {ans, i});
        }

        return ans;
    }
}
