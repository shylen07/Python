n=int(input())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(n):
    for j in range(n):
        print(arr[i][j]+1, end=" ")
    print()