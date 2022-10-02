# Factorial of a number
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
# print(factorial(5))

# fibnoacci number
def fib(n) :
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# print(fib(6))

# Powerset
def powerset(s):
    x = len(s)
    for i in range(1<<x):
        c=[]
        for j in range(x):
            if i &(1<<j):
                c.append(s[j])
        print(c)
# print(powerset([1,2,3]))

def powerset2(s):
    lists = [[]]
    for i in range(len(s)+1):
        for j in range(i):
            lists.append(s[j:i])
    return lists 
# print(powerset2([1,2,3]))




# Tower Of hanoi
def towerofhanoi(n, source, destination,helper):
    if n==1:
        print("Move disc1 from pole", source, "to" , destination)
        return
    towerofhanoi(n-1, source, helper, destination)
    print("Move disc", n, "from pole", source, "to pole", destination)
    towerofhanoi(n-1,helper, destination, source )

# print(towerofhanoi(2,'A','B','C'))

# Generate Permutation
def generatepermutation(str):
    def swap(i, j, s):
        arr = list(s)
        arr[i], arr[j]=arr[j], arr[i]
        s=""
        for i in arr:
            s+=i 
        return s

    def helper(pos, str, ans, n):
        if pos>=len(str):
            ans.append(str[:])
            return 
        for i in range(pos, len(str)):
            str = swap(pos, i, str)
            helper(pos+1, str, ans, n)
            str = swap(pos, i, str)
    ans = []
    n = len(str)
    helper(0, str, ans, n)
    return sorted(ans)
    

 
print(generatepermutation('abc')) 