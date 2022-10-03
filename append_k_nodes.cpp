#include<iostream>
#include<bits/stdc++.h>
using namespace std;

// Create A class node

class node{
    public:
    int data;
    node* next;

    // Node Class Constructor
    node(int val){
        data=val;
        next=NULL;

    }
};

// Insert Element At Tail

void insertAtTail(node* &head,int val){
    node* n=new node(val);
    if(head==NULL){
        head=n;
        return;
    }
    node* temp=head;
    while(temp->next!=NULL){
        temp=temp->next;
        }
        temp->next=n;
}


// Insert At Head

void insertAtHead(node* &head,int val){
    node* n=new node(val);
    n->next=head;
    head=n;
}

void print(node *head)
{
    node *temp = head;
    while (temp != NULL)
    {
        cout << temp->data << "->";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}
node* appendk(node* &head,int k){
    node* temp=head;
    node* start;
    int count=1;
    while(temp->next!=NULL){
        if(count==k)start=temp;
        temp=temp->next;
        count++;
    }
    node* newhead=start->next;
    start->next=NULL;
    temp->next=head;
    return newhead;
}
int main()
{
    node *head = NULL;
    insertAtTail(head, 1);
    insertAtTail(head, 2);
    insertAtTail(head, 3);
    insertAtTail(head, 4);
    insertAtTail(head, 5);
    insertAtTail(head, 6);
    print(head);
    
    node*newhead = appendk(head,3);
    print(newhead);

    //    deleteHead(head);
    //    print(head);

    return 0;
}
