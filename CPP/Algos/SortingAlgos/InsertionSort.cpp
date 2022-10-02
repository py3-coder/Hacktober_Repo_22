/*
Implemnting the Insertion sort.
Time Complexity = O(n^2);
Space Complexity = O(1);
*/

#include<iostream>
using namespace std;

int main(){
    int size;
    cin >> size;
    int array[size];
    
    cout << " Enter the Array : " << endl;
    for(int i = 0; i < size; i++){
        cin >> array[i];
    }
    int i = 1;
    while(i < size){
        int temp = array[i];
        int j = i - 1;
        while(j >= 0){

            if(array[j] > temp){
                array[j + 1] = array[j];
            }else{
                break;
            }
            j--;
        }
        array[j + 1] = temp;
        i++;
    }

    for(int i = 0; i < size; i++){
        cout << array[i] << " ";
    }
}