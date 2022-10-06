

class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        
        if(depth == 1){
            TreeNode* cur = new TreeNode(val);
            cur->left = root;
            return cur;
        }
        queue<TreeNode*>q;
        q.push(root);
        int level = 1;
        bool done = false;
        while(!q.empty()){
            int n = q.size();
            cout<<n;
            while(n--){
                TreeNode* cur = q.front();
                cout<<cur->val;
                q.pop();
                if(level == depth-1){
                    //add 
                    if(cur->left){
                        TreeNode* l = cur->left;
                        cur->left = new TreeNode(val);
                        cur->left->left = l;
                    }else{
                        cur->left = new TreeNode(val);
                    }
                    if(cur->right){
                        TreeNode* r = cur->right;
                        cur->right = new TreeNode(val);
                        cur->right->right = r;
                    }else{
                        cur->right = new TreeNode(val);
                    }
                    done = true;
                }else{
                    if(cur->left != NULL){
                        q.push(cur->left);
                    }
                    if(cur->right != NULL){
                        q.push(cur->right);
                    }
                }
            }
            level++;
            if(done) break;
        }
        return root;
    }
};