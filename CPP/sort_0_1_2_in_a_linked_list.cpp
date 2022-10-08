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

Node *sort012(Node *head)
{
   Node *curr=head;
   Node *zero=new Node(0);
   Node *one=new Node(0);
   Node *two=new Node(0);
   Node *tailz=zero;
   Node *tailo=one;
   Node *tailt=two; 
   while(curr!=NULL)
   {
       if (curr->data==0)
       {
          tailz->next=curr;
          tailz=tailz->next;
       }
       else if (curr->data==1)
       {
          tailo->next=curr;
          tailo=tailo->next;
       }
       else
       {
          tailt->next=curr;
          tailt=tailt->next;
       }
      curr=curr->next; 
   }
  if(one->next!=NULL)
   tailz->next=one->next;
  else
  tailz->next=two->next;
   
   tailo->next=two->next;
   tailt->next=NULL;
   
   return(zero->next);
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
    Node *head=new Node(2);
    head->next=new Node(1);
    head->next->next=new Node(2);
    head->next->next->next=new Node(2);
    head->next->next->next->next=new Node(1);
    print (head);
    cout<<endl;
    head=sort012(head);
    print(head);
    return 0;
}



