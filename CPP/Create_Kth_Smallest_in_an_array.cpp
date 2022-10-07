// C code for the above approach

#include <limits.h>
#include <stdio.h>

int partition(int arr[], int l, int r);

// This function returns K'th smallest element in arr[l..r]
// using QuickSort based method. ASSUMPTION: ALL ELEMENTS IN
// ARR[] ARE DISTINCT
int kthSmallest(int arr[], int l, int r, int K)
{
	// If k is smaller than number of elements in array
	if (K > 0 && K <= r - l + 1) {

		// Partition the array around last element and get
		// position of pivot element in sorted array
		int pos = partition(arr, l, r);

		// If position is same as k
		if (pos - l == K - 1)
			return arr[pos];
		if (pos - l > K - 1) // If position is more, recur
							// for left subarray
			return kthSmallest(arr, l, pos - 1, K);

		// Else recur for right subarray
		return kthSmallest(arr, pos + 1, r,
						K - pos + l - 1);
	}

	// If k is more than number of elements in array
	return INT_MAX;
}

void swap(int* a, int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

// Standard partition process of QuickSort(). It considers
// the last element as pivot and moves all smaller element
// to left of it and greater elements to right
int partition(int arr[], int l, int r)
{
	int x = arr[r], i = l;
	for (int j = l; j <= r - 1; j++) {
		if (arr[j] <= x) {
			swap(&arr[i], &arr[j]);
			i++;
		}
	}

	swap(&arr[i], &arr[r]);
	return i;
}

// Driver's code
int main()
{
	int N,K; cin>>N>>k;
  int arr[N];
  for(int i=0;i<N;i++){
    cin>>arr[i];
  }

	// Function call
	printf("K'th smallest element is %d",
		kthSmallest(arr, 0, N - 1, K));
	return 0;
}
