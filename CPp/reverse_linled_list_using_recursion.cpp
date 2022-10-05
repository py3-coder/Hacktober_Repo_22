#include <iostream>

using namespace std;
struct Node
{
    int data;
    Node *next;
    Node(int x)
    {
        data=x;
        next=NULL;
    }
};

Node *reverse(Node *head)
{
    if(head==NULL)
    return NULL;
    Node *curr=head;
    Node *prev=NULL;
    while(curr!=NULL)
    {
        Node *next=curr->next;
        curr->next=prev;
        prev=curr;
        curr=next;
    }
    return prev;
}
void print(Node *head)
{
    Node *temp=head;
    while(temp!=NULL)
    {
        cout<<(temp->data)<<" ";
        temp=temp->next;
    }
}


int main()
{
    Node *head=new Node(10);
    head->next=new Node(20);
    head->next->next=new Node(30);
    head->next->next->next=new Node(40);
    head->next->next->next->next=new Node(50);
    print(head);
    cout<<endl;
    head=reverse(head);
    print(head);
    return 0;
}



