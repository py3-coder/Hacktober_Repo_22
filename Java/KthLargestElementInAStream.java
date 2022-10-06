import java.util.NoSuchElementException;
import java.util.PriorityQueue;
import java.util.Scanner;
 
class MinHeap
{
    final PriorityQueue<Integer> pq;
    final int k;
 
    public MinHeap(int k)
    {
        this.k = k;
        pq = new PriorityQueue<>(k);
    }
 
    public int add(int n)
    {
        // if the min-heap's size is less than `k`, push the current element
        // into the min-heap
        if (pq.size() < k) {
            pq.add(n);
        }
 
        // otherwise, if the current element is more than the smallest element
        // in the min-heap, remove the smallest element from the heap and
        // push the current element
        else if (pq.peek() < n)
        {
            pq.poll();
            pq.add(n);
        }
 
        // if the size of the min-heap reaches `k`, return the top element
        if (pq.size() == k) {
            return pq.peek();
        }
        else {
            return -1;
        }
    }
}
 
class Solution
{
    public static MinHeap pq = null;
 
    // Function to find the k'th largest element in a stream
    public static int findKthLargest(int k, int nextInt)
    {
        // create MinHeap class instance first time when function is invoked
        if (pq == null) {
            pq = new MinHeap(k);
        }
 
        return pq.add(nextInt);
    }
}
 
class Main
{
    public static void main(String[] args)
    {
        int k = 3;
 
        Scanner in = new Scanner(System.in);
 
        // loop till the end-of-file (EOF) is reached
        while (true)
        {
            try {
                int nextInt = in.nextInt();
 
                int x = Solution.findKthLargest(k, nextInt);
                if (x != -1) {
                    System.out.println("The k'th largest element is " + x);
                }
            } catch (NoSuchElementException e) {
                break;
            }
        }
 
        in.close();
    }
}
