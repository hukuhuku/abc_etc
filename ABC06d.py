N = int(input())
c = []
for i in range(N):
    c.append(int(input()))
v = []
res = 0


def dfs(v,k=0):
    global res
    if k == N:
        if v == sorted(v):
            res = max(res,len(v))
            
    else:
        v.append(c[k])
        dfs(v,k+1)
        v.pop()
        dfs(v,k+1)

dfs(v)
print(N-res)
     
    
