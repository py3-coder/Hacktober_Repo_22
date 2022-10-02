// the concept is that when the rear and front reaches the end of queue we need to bring them to initial condition according to conditions.

#include<iostream>
using namespace std;

class circularQueue{
    public:
        int *arr;
        int front;
        int rear;
        int size;

        //constructor
        circularQueue(int size){
            this -> size = size;
            arr = new int[size];
            front = rear = -1; 
        }

        //behaviour or methods
        bool enqueue(int data){
            //condition to check if queue is full
            if((front == 0 && rear == size - 1) || (rear == (front - 1)%(size - 1))){
                cout<<"Queue is full"<<endl;
            }
            //to push first element
            else if(front == -1){
                front = rear = 0;
            }
            //to maintain cyclic nature
            else if(rear == size - 1 && front != 0){
                rear = 0;
            }
            //normal flow
            else{
                rear++;
            }

            arr[rear] = data;
            return true;
        }

        int dequeue(){
            //condition to check if queue is empty
            if(front == -1){
                cout<<"Queue is empty"<<endl;
                return -1;
            }
            //to store the data to be deleted
            int data = arr[front];
            //to delete the data
            arr[front] = -1;
            //single element is present
            if(front == rear){
                front = rear = -1;
            }
            //to maintain cyclic nature
            else if(front == size - 1){
                front = 0;
            }
            //normal flow
            else{
                front++;
            }
            return data;
        }
};

int main(){
    circularQueue queue1(5);

    queue1.enqueue(1);
    queue1.enqueue(2);
    queue1.enqueue(3);
    queue1.enqueue(4);
    queue1.enqueue(5);

    cout<<queue1.dequeue()<<endl;
    cout<<queue1.dequeue()<<endl;
    cout<<queue1.dequeue()<<endl;
    cout<<queue1.dequeue()<<endl;
    cout<<queue1.dequeue()<<endl;
    cout<<queue1.dequeue()<<endl;

    return 0;
}
