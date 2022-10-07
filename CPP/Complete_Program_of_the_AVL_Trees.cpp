#include <bits/stdc++.h>
using namespace std;

struct node
{
    node *left;
    node *right;
    int height;
    int data;
};
class Avl_class
{

protected:
    node *createNode(int value);
    int getBalanceFactor(node *ptr); // for finding the balance Factor.
    int getHeight(node *p);          // for getting the height of the tree.
    int maximumheight(int a, int b);
    node *leftRotation(node *x);  // for doing the left rotation.
    node *rightRotation(node *y); // for doing the right rotation.

public:
    node *insertion_In_AVL(node *root, int value);
    void Pre_Order_Traversal(node *ptr);
    void Post_Order_Traversal(node *ptr);
    void In_Order_Traversal(node *ptr);
};
int Avl_class::maximumheight(int a, int b)
{
    return a > b ? a : b; // ternary Operator is used for get the value of the maximum height.
}

node *Avl_class::rightRotation(node *y)
{
    cout << "    y       " << endl;
    cout << "  // \\       " << endl;
    cout << "  x   T3   We have to Rotate this Tree to the right in right Rotation." << endl;
    cout << "// \\         " << endl;
    cout << "T1  T2         " << endl;
    // In this case the root node is the y node then after ratation  the root node is the x node.
    // Intializing the value of the nodes.
    node *x = y->left;   // as in the given diagram.
    node *T2 = x->right; // as in the given diagram.

    // After the rotation  the senario will become.
    x->right = y; // As in the given diagram.
    y->left = T2; // As in the given diagram

    // After the rotation  the height of the tree will also be change then the height of the tree will be.
    x->height = maximumheight(getHeight(x->left), getHeight(x->right)) + 1; // for finding the change in height after the rotation is performed.
    y->height = maximumheight(getHeight(y->left), getHeight(y->right)) + 1;

    return x; // After the rotation the root node will be change to x node thus we will return .
}

node *Avl_class::leftRotation(node *x)
{
    cout << "    x       " << endl;
    cout << "  // \\       " << endl;
    cout << "  T1  y   We have to Rotate this Tree to the right in Left Rotation." << endl;
    cout << "    // \\   " << endl;
    cout << "    T2  T3  " << endl;
    // before rotation senario the value will be.
    node *y = x->right; // As in the given Diagram.
    node *T2 = y->left; // As in the given Diagram.

    // After rotation senario will be
    y->left = x;   // As in the given Diagram.
    x->right = T2; // As in the given Diagram.

    // After the rotation the height of the tree will also be change then we have to update the height of the tree.
    x->height = maximumheight(getHeight(x->left), getHeight(x->right)) + 1;
    y->height = maximumheight(getHeight(y->left), getHeight(y->right)) + 1;

    return y; // returning the root node.
}

node *Avl_class::insertion_In_AVL(node *root, int value)
{
    if (root == NULL)
    {
        return (createNode(value));
    }
    if (value > root->data)
    {
        root->right = insertion_In_AVL(root->right, value);
    }
    else if (value < root->data)
    {
        root->left = insertion_In_AVL(root->left, value);
    }
    root->height = maximumheight(getHeight(root->left), getHeight(root->right)) + 1;
    int balance_factor = getBalanceFactor(root);

    // The cases will be arised after the insertion all the balance point will be change then we have to maintain the stablity of the Avl tree then we have to do.
    // LL rotation Case.
    if (balance_factor > 1 && root->left->data > value)
    {
        root = leftRotation(root);
    }
    // RR rotation case.
    if (balance_factor < -1 && root->right->data < value)
    {
        root = rightRotation(root);
    }
    // LR rotation case.
    if (balance_factor > 1 && root->left->data < value)
    {
        root->left = leftRotation(root->left);
        root = rightRotation(root);
    }
    // RL rotation case.
    if (balance_factor < -1 && root->right->data > value)
    {
        root->right = rightRotation(root->right);
        root = leftRotation(root);
    }

    return root;
}

int Avl_class::getBalanceFactor(node *ptr)
{
    if (ptr == NULL)
    {
        return 0;
    }
    return (getHeight(ptr->left) - getHeight(ptr->right));
}

int Avl_class::getHeight(node *p)
{
    if (p == NULL)
    {
        return 0;
    }
    return p->height;
}

void Avl_class::In_Order_Traversal(node *ptr)
{
    if (ptr != NULL)
    {
        In_Order_Traversal(ptr->left);
        cout << ptr->data << endl;
        In_Order_Traversal(ptr->right);
    }
}
void Avl_class::Post_Order_Traversal(node *ptr)
{
    if (ptr != NULL)
    {
        Post_Order_Traversal(ptr->left);
        Post_Order_Traversal(ptr->right);
        cout << ptr->data << endl;
    }
}
void Avl_class::Pre_Order_Traversal(node *ptr)
{
    if (ptr != NULL)
    {
        cout << ptr->data << endl;
        Pre_Order_Traversal(ptr->left);
        Pre_Order_Traversal(ptr->right);
    }
}

// create Node Function Created
node *Avl_class::createNode(int value)
{
    node *newNode = new node;
    newNode->left = NULL;
    newNode->right = NULL;
    newNode->data = value;
    newNode->height = 1;
    return newNode;
}
int main()
{
    int choice;
    node *rootNode = NULL;
    Avl_class obj;
    do
    {
        cout << "1. Perform the Insertion in the AVL Tree" << endl;
        cout << "2. Do the Pre-Order Traversal" << endl;
        cout << "3. Do the Post-Order Traversal" << endl;
        cout << "4. Do the In-Order Traversal" << endl;
        cout << "5. Exit" << endl;
        cout << endl;
        cout << endl;
        cout << "Enter your choice:- ";
        cin >> choice;
        switch (choice)
        {
        case 1:
        {
            int value;
            cout << "Enter the value of the node:- ";
            cin >> value;
            rootNode = obj.insertion_In_AVL(rootNode, value);
            break;
        }
        case 2:
        {
            obj.Pre_Order_Traversal(rootNode);
            break;
        }
        case 3:
        {
            obj.Post_Order_Traversal(rootNode);
            break;
        }
        case 4:
        {
            obj.In_Order_Traversal(rootNode);
            break;
        }
        case 5:
        {

            break;
        }

        default:
            cout << "Wrong Choice Try Again !!!!!!!!!!!!!!!!!!" << endl;
            break;
        }

    } while (choice != 5);

    return 0;
}