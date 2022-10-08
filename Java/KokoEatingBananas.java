/*
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
*/

package com.company.Searching;
import java.util.ArrayList;
import java.util.Arrays;

public class KokoEatingBananas {
    static  int minEatingSpeed(int[] piles, int h){
        int arr[]= Arrays.copyOfRange(piles,0,piles.length);
        Arrays.sort(arr);
        int max=arr[arr.length-1];
        if(piles.length==h)
            return max;
        int s=1,e=max,n=piles.length;
        while (s<=e){
            int mid=s+(e-s)/2;
            int i=0,count=0;
            while (i<n){
                if(count>h)
                    break;
                if(piles[i]<=mid)
                    count=count+1;
                else {
                    if(count>h)
                        break;
                    int x=piles[i]/mid;
                    if(piles[i]%mid==0)
                        count=count+x;
                    else
                        count=count+x+1;
                }
                i++;
            }
            if(count<=h)
                e=mid-1;
            else
                s=mid+1;

        }
        return s;
    }

    public static void main(String[] args) {
        System.out.println(minEatingSpeed(new int[]{16,23,8,2,9},34));
    }
}
