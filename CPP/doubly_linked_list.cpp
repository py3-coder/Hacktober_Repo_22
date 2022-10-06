#include <iostream>
using namespace std;
class node
{
public:
    int data;
    node *next, *prev;
    node(int val)
    {
        data = val;
        next = NULL;
        prev = NULL;
    }
};
void insertAtHead(node *&head, int val)
{
    node *n = new node(val);
    node *temp = head;
    n->next = head;
    if (head != NULL)
    {
        head->prev = n;
    }
    head = n;
}
void insertAtTail(node *&head, int val)
{
    if (head == NULL)
    {
        insertAtHead(head, val);
        return;
    }
    node *n = new node(val);
    node *temp = head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = n;
    n->prev = temp;
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
void deleteHead(node *&head)
{
    node *todelete = head;
    head = head->next;
    head->prev = NULL;
    delete todelete;
}
void deletion(node *&head, int val)
{

    node *temp = head;
    if (temp->data == val)
    {
        deleteHead(head);
        return;
    }

    while (temp != NULL && temp->data != val)
    {
        temp = temp->next;
    }
    temp->prev->next = temp->next;
    if (temp->next != NULL)
    {
        temp->next->prev = temp->prev;
    }
    delete temp;
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
    insertAtHead(head, 7);
    print(head);
    deletion(head, 6);
    print(head);
       deleteHead(head);
       print(head);

    return 0;
}
