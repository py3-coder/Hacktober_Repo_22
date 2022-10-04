def solve(n, arr):
    # CODE HERE
    arr2 = list(set(arr))
    arr2.sort()
    return arr2[-2]

if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))
	res = solve(n, arr)
	print(res)
