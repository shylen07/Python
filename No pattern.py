n=5
for i in range(n):
    for j in range(n):
        if j==0 or j==i or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

print()

for i in range(n):
    for j in range(n):
        if j==0 or i==0 or j==n-1 or i==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()