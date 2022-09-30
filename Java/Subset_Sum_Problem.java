/*
Dynamic Programming
Subset_Sum_Problem 
*/

import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    int arr[] ={2,3,7,8,10};
	    int n=arr.length;
	    int sum=11;
		System.out.println(Subset_sum(arr,n,sum));
	}
	// Subset_sum Using Recursion 
	// TC : 2^n 
	// SC : O(1) + ~ O(2n) --> Auxilary Space for recusive call ---
	public static boolean Subset_sum(int arr[] ,int n,int sum){
	    if(sum==0){
	        return true;
	    }
	    if(sum!=0 && n==0){
	        return false;
	    }
	    if(arr[n-1]>sum){
	        return  Subset_sum(arr,n-1,sum);
	    }
	    return Subset_sum(arr,n-1,sum-arr[n-1]) || Subset_sum(arr,n-1,sum) ;
	}
}
