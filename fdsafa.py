from bisect import bisect 
N,C = list(map(int,input().split()))
L = []
for i in range(N):
    L.append(int(input()))

L = sorted(L)

for i in range(N//2):
    b = C-1 - L[i]
    n = bisect(L,b)#b <= a+1+Cとなるindexを取得

    if n < len(L) and i < n-1:
        L[i] = 0
        L.pop(n-1)
    elif len(L) <=  n:
        L[i] = 0
        L.pop() 

print(len(L))



