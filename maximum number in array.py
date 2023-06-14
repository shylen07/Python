n=int(input())
arr = list(map(int,input().split()))
di={}
for i in arr:
    di[i] = di[i]+1
m=max(di.values())
for k in di:
    if di[k]==m:
        print(k)
        break
              
