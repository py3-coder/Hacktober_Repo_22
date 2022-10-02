/*Program to implement Linear search Algo.

Algo:
1: intialize target;
2: start traversing the array one by one and comparing each 
with target.
3: if found return the index;
4: else repet step 2.
5:end

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

int linearSearch(int array[], int size, int target){

    for(int i = 0; i < size; i++){
        if(target == array[i]){
            return i;
        }
    }
    return -1;
}

int main(){
    int size, target;
    cin >> size;
    int array[size];
    readArray(array, size);
    cin >> target;

    cout << "Element found at index " << linearSearch(array, size, target);

    return 0;
}