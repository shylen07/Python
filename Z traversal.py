tc = int(input())
while tc:
    n = int(input())
    arr = []
    for i in range(n):
        row = list(map(int, input().split()))
        arr.append(row)

    for i in range(n):
        for j in range(n):
            if i ==n-1 or i==0  or i + j == n-1:
                print(arr[i][j], end =" ")
    tc-=1
print()

