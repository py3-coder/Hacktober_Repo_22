struct priority_queue {
char *key; // the key is the unique identifier of the object
int priority; // the priority value represents the priority of the object
};
The Priority Scheduling Program
Priority Scheduling Program is implemented using a Priority Queue.
// Function to insert a new element into the queue
void insert(int key, int priority)
{
priority_queue pq;
pq.key = malloc(sizeof(int));
pq.key = key;
pq.priority = priority;
pq.key = pq.key + 1;
if(pq.key == NULL) // If the key is already present
{
pq.key = pq.key + 1; // then add a new element
pq.priority = priority;
}
else // Otherwise, add the new element
{
pq.priority = priority;
}
}
// Function to delete the minimum key from the queue
void delete_min()
{
priority_queue pq;
pq.key = malloc(sizeof(int));
pq.key = pq.key - 1;
pq.priority = pq.priority - 1;
free(pq.key);
}
// Function to print the contents of the queue
void print_queue(priority_queue pq)
{
int i;
for(i = 0; i < pq.key; i++)
printf("%d ", pq.priority);
printf("\n");
}
/*
Program to demonstrate the Priority Queue
*/
// Driver Program to demonstrate the Priority Queue
int main()
{
int key;
priority_queue pq;
printf("Enter the key of an item to be inserted into the queue : ");
scanf("%d", &key);
insert(key, 10);
print_queue(pq);
delete_min();
print_queue(pq);
return 0;
}
