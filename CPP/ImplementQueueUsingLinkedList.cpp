// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

struct QueueNode
{
    int data;
    QueueNode *next;
    QueueNode(int a)
    {
        data = a;
        next = NULL;
    }
};

struct MyQueue {
    QueueNode *front;
    QueueNode *rear;
    void push(int);
    int pop();
    MyQueue() {front = rear = NULL;}
};



int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        MyQueue *sq = new MyQueue();

        int Q;
        cin>>Q;
        while(Q--){
        int QueryType=0;
        cin>>QueryType;
        if(QueryType==1)
        {
            int a;
            cin>>a;
            sq->push(a);
        }else if(QueryType==2){
            cout<<sq->pop()<<" ";

        }
        }
        cout<<endl;
    }
    }
// } Driver Code Ends


//Function to push an element into the queue.
void MyQueue:: push(int x)
{
        // Your Code
        QueueNode *temp=new QueueNode(x);
        if(front==0 and rear==0){
            front=rear=temp;
        }
        else{
            rear->next=temp;
            rear=rear->next;
        }
}

//Function to pop front element from the queue.
int MyQueue :: pop()
{
        // Your Code       
         if(front==0 and rear==0){
            return -1;
        }
        QueueNode *temp;
        if(front==rear){
            temp=front;
            front=rear=NULL;
            int x=temp->data;
            delete temp;
            return x;
        }
            temp=front;
            front=front->next;
            int x=temp->data;
            delete temp;
            return x;
}
