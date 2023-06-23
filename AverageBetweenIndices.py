def solve(n, arr, x, y):
    ''' arr =[]
    n = int(input())
    for i in range(n):
        a = int(input())
        arr.append(a)
    x = int(input())
    y = int(input()) '''
    lst_new = arr[x:y+1]
    avg = sum(lst_new)/len(lst_new)
    return avg



if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))
	x = int(input())
	y = int(input())
	res = solve(n, arr, x, y)
	print(res)
