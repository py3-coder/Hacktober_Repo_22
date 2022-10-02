/*
Implemnting Bubble Sort.

Time Complexity = O(n^2);
Space Complexity = O(1);
*/

#include<iostream>
using namespace std;

int main(){
    int size;
    cin >> size;
    int array[size];
    cout << "Enter the Elements : "<< endl;
    
    for(int i = 0; i < size; i++){
        cin >> array[size];
    }

    for(int i = 1; i < size; i++){
        for(int j = 0; j < size - i; j++){

            if(array[j] > array[j + 1]){
                swap(array[j], array[j + 1]);
            }
        }
    }

    for(int i = 0; i < size; i++){
        cout << array[i] << " ";
    }

    return 0;
}