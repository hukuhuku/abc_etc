n = int(input())
a = [0 for i in range(n)]
a[2] = 1

def dfs (i,k):
    global a
    a[i] = a[i-1] + a[i-2] + a[i-3]
    if i == k:
        return
    dfs(i+1,k)
dfs(3,n-1)
print(a[n-1]%10007)