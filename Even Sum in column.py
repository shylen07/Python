n, m= map(int,input().split())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(m):
    sum=0
    for j in range(n):
        if arr[j][i]%2==0:
            sum+=arr[j][i]
    print(sum)
