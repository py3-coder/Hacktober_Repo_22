#include <iostream>
using namespace std;

void printArray(int A[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
}

void BubbleSort(int *A, int n)
{
    int temp;
    for (int i = 0; i < n - 1; i++)
    {
        bool status = false;

        for (int j = 0; j < n - i - 1; j++)
        {
            status = true;

            if (A[j] > A[j + 1])
            {
                temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
        if (!status)
            break;
    }
}

int main()
{
    int arr[] = {5, 7, 3, 1, 2};
    int n = 5;
    printArray(arr, n);
    BubbleSort(arr, n);
    printArray(arr, n);
}