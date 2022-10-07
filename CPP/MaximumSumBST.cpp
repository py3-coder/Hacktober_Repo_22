#include<bits/stdc++.h>
int ans=0;
vector<int>helper(TreeNode* root){
        if(!root)
            return {0,INT_MAX,INT_MIN};//because leafNode satisfy always
        // so for from below leafNode we return such data that it always satisfy 
        // (currRoot->val>left_Max(left tree max value) and curRoot->val<right_min(right subtree MIN value)) thats why we return 
        //     (0,INT_MAX,INT_MIN)~~(sum,left,right)
        
        auto l=helper(root->left);
        
        auto r=helper(root->right);
        
        int sum=l[0]+r[0]+root->val;
        
        
        if(root->val>l[2]&&root->val<r[1]){
            ans=max(ans,sum);
            return {sum,min(l[1],root->val),max(r[2],root->val)};
        }
        else
        {
            // if  condition for BSt is invalid then we return such value so that 
            //     for all node above no bst is possible           
            
            return {0, INT_MIN, INT_MAX};   
        }
                
    }   
    

int solve(TreeNode* root){
    helper(root);
    return ans;
}
