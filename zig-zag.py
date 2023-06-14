n, m = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
for i in range(n):
    if i % 2 == 0:   
        for j in range(m-1,-1,-1):
            print(arr[i][j], end=" ")
    else:
        for j in range(m):
            print(arr[i][j], end=" ")