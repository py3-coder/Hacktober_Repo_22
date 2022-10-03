#include<bits/stdc++.h>

using namespace std;

long long int binarysearch(int n){
        int low  =0;
        int high = n;
        long long int mid = low+(high-low)/2;
        long long int ans  = -1;
        while(low<=high){
            long long int square =  mid*mid;
            if(square == n){
                return mid;
            }
            else if(square>n){
                high = mid-1;
            }
            else{
                ans = mid;
                low = mid+1;
                
            }
            mid = low+(high-low)/2;
        }
        return ans;
    }
double moreprecision(int n,int precision,int tempsol){
    double factor =  1;
    double ans = tempsol;
    for(int i = 0;i<precision;i++){
        factor  = factor/10;
        for(double j =  ans;j*j < n;j = j+factor){
            ans = j;
        }

    }
    return ans;
}

int main()
{
    int n;
    cin>>n;


    int tempsol  = binarysearch(n);
    // cout<<tempsol<<setprecision(4)<<endl;
    cout<<moreprecision(n,4,tempsol)<<endl;
    
    return 0;
}
