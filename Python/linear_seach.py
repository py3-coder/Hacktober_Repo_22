''' linear search is a searching technique used to search an element linearly'''
from unittest import result


def linear_search(mylist,item):
    for i in range(len(mylist)):
        if mylist[i]==item:
            return i
    return -1
mylist=[]
n=int(input("enter the number of elements in list\n"))
print("enter the elemnts into list\n")
for i in range(n):
    mylist.append(int(input()))
print("mylist is created %s"%(mylist))
print("elements in the list",mylist)
x=int(input("enter the searching element"))
result =linear_search(mylist,x)
if (result==-1):
    print("element can not be found")
else:
    print(f"element {x} is present in position {result}")                    