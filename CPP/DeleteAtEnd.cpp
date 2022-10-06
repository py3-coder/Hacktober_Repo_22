#include <iostream>
using namespace std;

struct node {
    int num;
    struct node * next;
}*head;
void deleteEnd()//fuction to delete last node from the circular linked list
{
       struct node *cur,*prev;
		cur=head;
		while(cur->next!=head)
		{
			prev=cur;
			cur=cur->next;
		}
		prev->next=head;
		free(cur);
}
void build(int n)//function to build circular linked list
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
    cout<<"\nAfter deleting last node, new list is:";  
    deleteEnd();
    display();	
    return 0;
}
