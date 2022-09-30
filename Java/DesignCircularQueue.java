class MyCircularQueue {
    int[] myQueue;
    int front, rear, size;

    public MyCircularQueue(int k) {
        myQueue = new int[k];
        front = -1;
        rear = -1;
        size = k;
    }
    
    public boolean enQueue(int value) {
        if(isFull())
            return false;
        if(rear==-1) {
            front=0;
            rear=0;
            myQueue[rear] = value;
        }
        else if((front!=0) && (rear==size-1)) {
            rear = 0;
            myQueue[0] = value;
        }
        else {
            ++rear;
            myQueue[rear] = value;
        }
        return true;
    }
    
    public boolean deQueue() {
        if(isEmpty())
            return false;
        
        if(front==rear) {
            front = -1;
            rear = -1;
        }
        else if(front == size-1)
            front = 0;
        else
            ++front;
        
        return true;
    }
    
    public int Front() {
        if(isEmpty())
            return -1;
        return myQueue[front];
    }
    
    public int Rear() {
        if(isEmpty())
            return -1;
        return myQueue[rear];        
    }
    
    public boolean isEmpty() {
        return front==-1;
     }
    
    public boolean isFull() {
        return (rear+1)%size == front;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
