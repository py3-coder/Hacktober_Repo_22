#include<bits/stdc++.h>
#include<conio.h>
using namespace std;
#define M 4
#define N 4
void displayMatrix(int matrix[][N])
{
	for(int i=0; i<M; i++)
	{
		for(int j=0; j<N; j++)
		{
			cout<<matrix[i][j]<<" ";
		}
		cout<<endl;
	}
}
void SpiralMatrix(int matrix[][N])
{
	int top = 0; // Rows traversing
	int bottom = M-1;  // starting row to last row
	int left = 0; // starting column 
	int right = N-1; // last column
	while(top<=bottom && left<=right)
	{
		for(int i = left; i<=right; i++)
		{
			cout<<matrix[top][i]<<" ";
		}
		top++;
		for(int j = top; j<=bottom; j++)
		{
			cout<<matrix[j][right]<<" ";
		}
		 right--;
		if(bottom>=top) // edge cases handle
		{
			for(int k = right; k>=left; k--)
			{
				cout<<matrix[bottom][k]<<" ";
			}
			bottom--;
		}
		
		if(right>=left)
		{
			for(int l = bottom; l>=top; l--)
			{
				cout<<matrix[l][left]<<" ";
			}
			left++;
		}
	}
}
int main()
{
	int matrix[M][N]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
	displayMatrix(matrix);
	cout<<"After spirally tranversing: "<<endl;
	SpiralMatrix(matrix);
	getch();
	return 0;
	
}