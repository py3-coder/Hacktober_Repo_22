import numpy as np
def check(i):
for j in range(no_r):
if(needed[i][j]>available[j]):
return 0
return 1
no_p = 5
no_r = 4
Sequence = np.zeros((no_p,),dtype=int)
visited = np.zeros((no_p,),dtype=int)
allocated = np.array([[4,0,0,1],[1,1,0,0],[1,2,5,4],[0,6,3,3],[0,2,1,2]])
maximum = np.array([[6,0,1,2],[1,7,5,0],[2,3,5,6],[1,6,5,3],[1,6,5,6]])
needed = maximum - allocated
available = np.array([3,2,1,1])
count = 0
while( count < no_p ):
temp=0
for i in range( no_p ):
if( visited[i] == 0 ):
if(check(i)):
Sequence[count]=i;
count+=1
visited[i]=1
temp=1
for j in range(no_r):
available[j] += allocated[i][j]
if(temp == 0):
break
if(count < no_p):
print('The system is Unsafe')
else:
print("The system is Safe")
print("Safe Sequence: ",Sequence)
print("Available Resource:",available)
import numpy as np def check(i): for j in range(no_r): if(needed[i][j]>available[j]): return 0 return 1 no_p = 5 no_r = 4 Sequence = np.zeros((no_p,),dtype=int) visited = np.zeros((no_p,),dtype=int) allocated = np.array([[4,0,0,1],[1,1,0,0],[1,2,5,4],[0,6,3,3],[0,2,1,2]]) maximum = np.array([[6,0,1,2],[1,7,5,0],[2,3,5,6],[1,6,5,3],[1,6,5,6]]) needed = maximum - allocated available = np.array([3,2,1,1]) count = 0 while( count < no_p ): temp=0 for i in range( no_p ): if( visited[i] == 0 ): if(check(i)): Sequence[count]=i; count+=1 visited[i]=1 temp=1 for j in range(no_r): available[j] += allocated[i][j] if(temp == 0): break if(count < no_p): print('The system is Unsafe') else: print("The system is Safe") print("Safe Sequence: ",Sequence) print("Available Resource:",available)
import numpy as np

def check(i):
    for j in range(no_r):
        if(needed[i][j]>available[j]):
            return 0
    return 1


no_p = 5
no_r = 4

Sequence = np.zeros((no_p,),dtype=int)
visited = np.zeros((no_p,),dtype=int)

allocated = np.array([[4,0,0,1],[1,1,0,0],[1,2,5,4],[0,6,3,3],[0,2,1,2]])
maximum = np.array([[6,0,1,2],[1,7,5,0],[2,3,5,6],[1,6,5,3],[1,6,5,6]])

needed = maximum - allocated
available = np.array([3,2,1,1])

count = 0
while( count < no_p ):
    temp=0
    for i in range( no_p ):
        if( visited[i] == 0 ):
            if(check(i)):
                Sequence[count]=i;
                count+=1
                visited[i]=1
                temp=1
                for j in range(no_r):
                    available[j] += allocated[i][j] 
    if(temp == 0):
        break


if(count < no_p):
    print('The system is Unsafe')
else:
    print("The system is Safe")
    print("Safe Sequence: ",Sequence)
    print("Available Resource:",available)
   

