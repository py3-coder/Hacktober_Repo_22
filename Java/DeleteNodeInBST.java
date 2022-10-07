/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class DeleteNodeInBST {
    public TreeNode deleteNode(TreeNode root, int key) {
        // if root is null then return 
        if(root == null) return root;
        // if key is smaller then delete on left 
        if(root.val > key){
            root.left  = deleteNode(root.left , key);
        }else if(root.val < key){
            root.right = deleteNode(root.right , key);
        }
        // if we found thenode to be deleted then
        else{
            // case 1 : if it's left child is null then return right child
            if(root.left == null) return root.right;
            // case 2 : if it's right child is null then return left child
            else if(root.right == null) return root.left;
            // case 3 : if both childs are not null then
            
            // set the node to be deleted's value to left most predecessor
            // root's right child
            root.val = leftPred(root.right);
            // and now delete the left most predecessor from root.right sub tree
            // here we are deleting coz we know that to delete a 
            //  left most predecessor is easy coz it's left child is always a null
            root.right = deleteNode(root.right , root.val);
        }
        // return the root
        return root;
    }
    public int leftPred(TreeNode root){
        // take root's val
        int predVal = root.val;
        // go to left until its not null
        while(root.left != null){
            predVal = root.left.val;
            root = root.left;
        }
        // return the value of the predecessor
        return predVal;
    }
}
