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

Node *findMiddle(Node *head)
{
    if(head==NULL)
    return NULL;
    Node *first=head;
    Node *second=head;
    for(first=head;first!=NULL&&first->next!=NULL;first=first->next->next)
    second=second->next;

    return second;
}

bool palindrome(Node *head)
{
   Node* middle=findMiddle(head);
   Node* curr=middle;
   Node* prev=NULL;
   while (curr!=NULL)
   {
       Node *next=curr->next;
       curr->next=prev;
       prev=curr;
       curr=next;
   }
   curr=head;
   while(prev!=NULL)
   {
   if(curr->data!=prev->data)
   return false;
   else
   {
       curr=curr->next;
       prev=prev->next;
   }
   }
   return true;
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
    head->next->next->next=new Node(20);
    head->next->next->next->next=new Node(10);
    print(head);
    cout<<endl;
    bool b=palindrome(head);
    cout<<b;
    return 0;
}
