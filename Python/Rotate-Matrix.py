# program to rotate matrix clockwise and anticlockwise

def Transpose(A):
    for i in range(len(A[0])):
        for j in range(i,len(A)):
             A[i][j],A[j][i]=A[j][i],A[i][j]
    
def clockwise(A):
    Transpose(A)
    i=0
    j=len(A)-1
    while(i<j):
        for k in range(len(A)):
            A[k][i],A[k][j]=A[k][j],A[k][i]
        i+=1
        j-=1
def anticlockwise(A):
    Transpose(A)
    i=0
    j=len(A)-1
    while(i<j):
        A[i],A[j]=A[j],A[i]
        i+=1
        j-=1
m=int(input("Enter nubmer of rows of matrix"))
A=[]
for i in range(m):
    print("Enter row number",i+1)
    temp=list(map(int,input().split()))
    A.append(temp)
for i in A:
        print(i)
print("    ")
C=int(input("Enter 1 for clockwise 2 for anticlockwise"))
if C==1:
    clockwise(A)
else:
    anticlockwise(A)
for i in A:
        print(i)
