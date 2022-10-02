/*
Algorithm
Step 1 − Set MIN to location 0
Step 2 − Search the minimum element in the list
Step 3 − Swap with value at location MIN
Step 4 − Increment MIN to point to next element
Step 5 − Repeat until list is sorted

Pseudocode
procedure selection sort 
   list  : array of items
   n     : size of list

   for i = 1 to n - 1
    set current element as minimum
      min = i    
  
      check the element to be minimum 

      for j = i+1 to n 
         if list[j] < list[min] then
            min = j;
         end if
      end for

      swap the minimum element with the current element
      if indexMin != i  then
         swap list[min] and list[i]
      end if
   end for
	
end procedure

Time Complexity = O(n^2);
Space Complexity = O(1);
*/

#include<iostream>
using namespace std;

void readArray(int array[], int size){
    for(int i = 0 ; i < size; i++){
        cin >> array[i];
    }
}

void printArray(int array[], int size){
        for(int i = 0 ; i < size; i++){
            cout << array[i] << " ";
        }
}

void selectionSort(int array[], int size){
    for(int i = 0; i < size - 1; i++){
        int minIndex = i;

        for(int j = i + 1; j < size; j++){
            if(array[j] < array[minIndex]){
                minIndex = j;
            }
        }
        swap(array[minIndex], array[i]);
    }
}

int main(){
    int size;
    cin >> size;
    int array[size];
    cout << "Enter the Elements of the Array. " << endl;
    readArray(array, size);
    selectionSort(array, size);
    printArray(array, size);


}