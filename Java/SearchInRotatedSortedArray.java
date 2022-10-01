
/******************************************************************************
 Leet Code :33. Search in Rotated Sorted Array
 Link : https://leetcode.com/problems/search-in-rotated-sorted-array/
 *******************************************************************************/

class SearchInRotatedSortedArray {
    // This is an example of binarySearch problem

    public int search(int[] nums, int target) {
        int pivot = pivotElement(nums);
        int bin = binarySearch(nums,target,0,pivot);
        if(bin!=-1){
            return bin;
        }
        else{
            return binarySearch(nums,target,pivot+1,nums.length-1);
        }

    }

    // If we can find the pivot element then we can easly aoply binary search in left and right of
    // pivot element .

    int pivotElement(int[] array) {
        int start = 0;
        int end = array.length - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (mid < end && array[mid] > array[mid + 1]) {
                return mid;
            }

            if (mid > start && array[mid] < array[mid - 1]) {
                return mid - 1;

            }
            if (array[start] > array[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;

            }

        }
        return -1;
    }

    int binarySearch(int[] nums, int target, int start, int end){

        while(start<=end){
            int mid = start + (end - start)/2;

            if(nums[mid]==target){
                return mid;

            }

            else if(nums[mid]>target){

                end =mid -1;
            }

            else{
                start = mid + 1;
            }
        }
        return -1;
    }
}