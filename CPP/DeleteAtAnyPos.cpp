#include <iostream>
using namespace std;

struct node {
    int num;
    struct node * next;
}*head;
void deleteSpecific(int pos)//function to delete any node from the list
{             
        struct node *p,*q;
        int del,k=0;
        del=pos-1;
        p=head;
        while(k!=del)
        {
            q=p;
            p=p->next;
            k++;
        }
        q->next=p->next;
        free(p);//deleting specific node
}
void build(int n)//function to build linked list
{
    int i, num;
    struct node *preptr, *newnode;

    if(n >= 1)
    {
        head = (struct node *)malloc(sizeof(struct node));

        cout<<"Enter data of the list:\n";
        cin>>num;
        head->num = num;
        head->next = NULL;
        preptr = head;
        for(i=2; i<=n; i++)
        {
            newnode = (struct node *)malloc(sizeof(struct node));
            cin>>num;
            newnode->num = num;
            newnode->next = NULL;	
            preptr->next = newnode;	
            preptr = newnode;   		
        }
        preptr->next = head; 		//linking last node with head node
    }
}
void display()//function to display list
{
    struct node *tmp;
    int n = 1;
    
    if(head == NULL)
    {
        cout<<"List is empty";
    }
    else
    {
        tmp = head;
        
        cout<<"\nCircular linked list data:\n";
        do {
            cout<<tmp->num<<" ";
            tmp = tmp->next;
            n++;
        }while(tmp != head);
    }
}
int main()//main function
{
    int n,pos;
    head = NULL;
    cout<<"Enter the size of circular linked list: ";
    cin>>n;
    build(n); 
    display();
    cout<<"\nEnter position from where you want to delete the node: ";
    cin>>pos;
    cout<<"\nAfter deleting node from specific position, new list is:";  
    deleteSpecific( pos);
    display();	
    return 0;
}
