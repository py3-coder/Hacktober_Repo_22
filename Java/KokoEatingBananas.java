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
