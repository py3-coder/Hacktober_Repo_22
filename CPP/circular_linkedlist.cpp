#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Node
{
public:
    int data;
    Node *next;
    Node() {}
    Node(int value)
    {
        data = value;
    }
};
void insertathead(Node **last, int value)
{
    Node *newnode = new Node(value);
    if ((*last) == NULL)
    {
        *last = newnode;
        newnode->next = *last;
        return;
    }
    Node *hd = (*last)->next;
    newnode->next = hd;
    hd = newnode;
}
void insertatend(Node **last, int value)
{
    Node *newnode = new Node(value);
    if ((*last) == NULL)
    {
        *last = newnode;
        newnode->next = *last;
        return;
    }
    newnode->next = (*last)->next;
    (*last)->next = newnode;
    *last = newnode;
}
void insertatpos(Node **last, int pos, int value)
{
    Node *newnode = new Node(value);
    if ((*last) == NULL)
    {
        *last = newnode;
        newnode->next = *last;
        return;
    }
    int index = pos - 1;
    Node *temp = (*last)->next;
    for (int i = 0; i < index - 1; i++)
    {
        temp = temp->next;
    }
    newnode->next = temp->next;
    temp->next = newnode;
}
void deleteathead(Node **last)
{
    if (*last == NULL)
    {
        cout << "Linked list is already empty" << endl;
    }
    Node *hd = (*last)->next;
    hd = hd->next;
    (*last)->next = hd;
    cout << "The node has been deleted" << endl;
}
void deleteatlast(Node **last)
{
    if (*last == NULL)
    {
        cout << "linked list is already empty" << endl;
    }
    Node *temp = (*last)->next;
    while (temp->next != *last)
    {
        temp = temp->next;
    }
    temp->next = (*last)->next;
    *last = temp;
}
void deleteatpos(Node **last, int pos)
{
    if (*last == NULL)
    {
        cout << "linked list is already empty" << endl;
    }
    int index = pos - 1;
    Node *temp = *last, *temp2;
    for (int i = 0; i < index - 1; i++)
    {
        temp2 = temp;
        temp = temp->next;
    }
    temp2->next = temp->next;
}
int main()
{

    return 0;
}
