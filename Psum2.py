n = 3
a = [3,5,8]
m = [3,2,2]
K = 17


dp = [[False for i in range(K+1)]for i in range(n+1)]

for i in range(n+1):
    for j in range(K+1):
        for k in range(m[i]):
            if k*a[i] < j :
                 dp[i][j] = dp[i-1][j-k*a[i]] 
                 if dp[i][j]:
                     break
                