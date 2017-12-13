N = int(input())
a = list(map(int,input().split()))


for i in range(N):
    res = 1
    while res == 1:
        if a[i] != 1:
            a[i] = a[i]/2
        if a[i]%2 == 1 or a[i] == 2:
            res = 0
ans = len(set(a))
print(ans)        
    
