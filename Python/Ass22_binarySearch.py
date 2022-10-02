#NAME : NITISH KUMAR MAURYA
#GITHUB : github.com/MauryaNitish65/
#INSTITUTE/COMPANY : HALDIA INSTITUTE OF TECHNOLOGY
#DOMAIN: IT
#binary search
def binarySearch(list1,l,h,k):
    if(l<=h):
        m=(int)((l+(h-l)//2))
        if list1[m]==k:
            return m
        elif list1[m]>k:
            return binarySearch(list1,l,m-1,k)
        else:
            return binarySearch(list1,m+1,h,k)
    return -1;
n=int(input("No of elements "))
list2=[]
print("Enter elements ")
for i in range(n):
    list2.append(int(input()))
p=int(input("Element to be searched "))
k=binarySearch(list2,0,n-1,p)
if k==-1:
    print(p," not found ")
else:
    print(p," is at index ",k)
