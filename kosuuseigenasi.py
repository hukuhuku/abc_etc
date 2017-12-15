#n = int(input())
#w = []
#v = []
#for i in range(n):
#    a,b = list(map(int,input().split()))
#    w.append(a)
#    v.append(b)
#W = int(input())
n = 3
w = [3,4,2]
v = [4,5,3]
W = 7
dp = [[0 for i in range(W+1)] for i in range(n+1)]


for i in range(n):
    for j in range(W+1):
        if j < w[i]:
           dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j],dp[i+1][j-w[i]]+v[i])  

print(dp)             