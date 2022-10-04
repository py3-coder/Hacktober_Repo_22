#include<bits/stdc++.h>
using namespace std;
void swap(int &a,int &b)
{
    int tem=b;
    b=a;
    a=tem;
}
int lomutoPartition(int a[],int l,int h)
{
    int pivot=a[h];
    int i=(l-1);
    for(int j=l;j<=h-1;j++)
        if(a[j]<pivot)
        {
            i++;
            swap(a[i],a[j]);
        }
    swap(a[i+1],a[h]);
    return i+1;
}
void qsort(int a[],int l,int h)
{
    if(h>l)
    {
        int p=lomutoPartition(a,l,h);
        qsort(a,l,p-1);
        qsort(a,p+1,h);
    }
}
int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
        cin>>a[i];
    qsort(a,0,n-1);
    for(int i=0;i<n;i++)
        cout<<a[i]<<" ";
}
