import java.util.*;
public class SlidingWindow {   
    
    public static int maxConsec_KSum(int arr[], int k) {     // Fixed Size Variable Window. Here, first we achieve window size and then slide it to satisfy the condition.
        int currSum=0;
        for (int i = 0; i < k; i++) {
            currSum += arr[i];
        }
        int maxSum = currSum;
        for (int i = k; i < arr.length; i++) {
            currSum += (arr[i] -arr[i-k]);
            maxSum = Math.max(currSum, maxSum);
        }
        return maxSum;
    }
    public static int lenOfLongSubarrboth (int A[], int N, int K) { // VAriable Size window, hashmap is used, first the sum is calculated till the given k then checked whether hashmap contains it or not.
        //This solution is for both +ve and -ve Numbers 
        HashMap<Integer,Integer> map = new HashMap<>(); // TC and SC :- O(n)
        int sum = 0, max = 0;
        
        for(int i = 0; i < N; i++) {
            sum += A[i];
            
            if(sum==K)  max = i+1;
            
            if(!map.containsKey(sum)) {
                map.put(sum,i);
            }
            
            if(map.containsKey(sum-K)) {
                if(max < i - map.get(sum-K))
                    max = i - map.get(sum-K);
            }
        }
        return max;
    }
    static int lenOfLongSubarrpositive(int A[], int N, int K)
  {
 //This solution is for positive num only, variable size window
    int i = 0, j = 0, sum = 0;
    int maxLen = Integer.MIN_VALUE;
 
    while (j < N) {
      sum += A[j];
      if (sum < K) {
        j++;
      }
      else if (sum == K) {
        maxLen = Math.max(maxLen, j-i+1);
        j++;
      }
      else if (sum > K) {
        while (sum > K) {
          sum -= A[i];
          i++;
        }
        if(sum == K){
          maxLen = Math.max(maxLen, j-i+1);
        }
        j++;
      }
    }
    return maxLen;
  }
    public static void main(String[] args) {    //Driver Code
        Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        int k = sc.nextInt();
        System.out.println(maxConsec_KSum(arr,k));
        sc.close();
        
    }
}
