#include<bits/stdc++.h>
using namespace std;
#define ll long long int

void conquer(int a[], int si, int mid, int ei){
  auto *merged = new int[ei - si + 1];
  int ind1 = si, ind2 = mid + 1, x = 0;

  while(ind1 <= mid and ind2 <= ei){
    if(a[ind1] <= a[ind2]) merged[x++] = a[ind1++];
    else merged[x++] = a[ind2++];
  }

  while(ind1 <= mid) merged[x++] = a[ind1++];
  while(ind2 <= ei) merged[x++] = a[ind2++];

  int n = ei - si + 1;
  for(int i = 0, j = si; i < n; i++, j++) a[j] = merged[i];
  delete[] merged;
}

void divide(int a[], int si, int ei)
{
  if(si >= ei)  return; // base case
  auto mid = si + (ei - si) / 2;
  divide(a, si, mid);
  divide(a, mid + 1, ei);
  conquer(a, si, mid, ei);
}

int main(){
  int arr[] = {6, 3, 9, 5, 2};
  int n = sizeof(arr) / sizeof(arr[0]);
  divide(arr, 0, n - 1);
  for(int i = 0; i < n; i++) cout << arr[i] << " ";
  cout << endl;
  return 0;
}
