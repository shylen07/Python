tc = int(input())
while tc:
    n, m= map(int,input().split())

    arr = []
    for i in range(n):
        row = list(map(int, input().split()))
        arr.append(row)

    for i in range(n):
        for j in range(m):
            print(arr[i][j]+1, end=" ")
        print()
    tc-=1

