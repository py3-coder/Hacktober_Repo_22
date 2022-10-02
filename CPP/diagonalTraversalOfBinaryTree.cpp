#include <bits/stdc++.h>
using namespace std;

class Node {
    public:
        int data;
        Node *left, *right;

        Node(int d) {
            data = d;
            left = right = NULL;
        }
};

vector<int> diagonal(Node *root)
{
    // your code here
    vector<int> result;
    
    if(root == NULL)
        return result;
            
    queue<Node*> q;
    q.push(root);
    
    while(!q.empty()) {
        int size = q.size();
        vector<int> ans;
        
        while(size--) {
            Node *frontNode = q.front();
            q.pop();
            
            while(frontNode != NULL) {
                ans.push_back(frontNode->data);
                
                if(frontNode->left)
                    q.push(frontNode->left);
                    
                frontNode = frontNode->right;
            }
        }
        
        for(auto x:ans) {
            result.push_back(x);
        }
    }
    
    return result;
}