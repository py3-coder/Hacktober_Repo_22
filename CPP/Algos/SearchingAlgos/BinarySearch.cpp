/*Implementing Binary Search 

Algo:
1: Start;
2: Initalize start = 0 ans end = size - 1;
3: Find mid = start + (end - start) / 2;
4: Compare the Target 
5: IF tareget is greater then set start = mid + 1;
    ELSE 
        mid - 1;
6: Repete Step 5 Until Target is not found.
7: END;        

Time Complexity is O(log n);
Space Complexity = O(1);
*/
#include<iostream>

using namespace std;

void readArray(int array[], int size){
    cout << "Enter the Elements of the Array : "<< endl;
    for(int i = 0; i < size; i++){
        cin >> array[i];
    }
}

int binarySearch(int array[], int size, int target){
    int start = 0; 
    int end = size - 1;
    int mid;

    while(start <= end){
        mid = start + (end - start) / 2;

        if(array[mid] == target){
            return mid;
        }

        if(array[mid] > target){
            end = mid - 1;
        }else{
            start = mid + 1;
        }
    }
    return -1;
}

int main(){
    int size, target, index;
    cin >> size;
    int array[size];
    readArray(array, size);
    cout << "Enter the target Number " << endl;
    cin >> target;

    index = binarySearch(array, size, target);

    cout << "Target Present at index " << index << endl;

}