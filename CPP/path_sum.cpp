//Problem link - https://leetcode.com/problems/path-sum/description/


//inorder traversal
class Solution {
public:
    bool ans = false;

    void solve(TreeNode* root, int targetSum){
        
        if(!root->left and !root->right and targetSum == 0){
            ans = true;
            return;
        }
        if(root->left != NULL){
            solve(root->left, (targetSum - root->left->val));
        }
        if(root->right)
            solve(root->right, targetSum - root->right->val);
    }

    bool hasPathSum(TreeNode* root, int targetSum) {
        if(!root) return false;
        solve(root, targetSum - root->val);
        return ans;
    }
};