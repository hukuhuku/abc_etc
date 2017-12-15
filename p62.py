import numpy as np

n = int(input())
a = list(map(int(input().split())))
m = list(map(int,input().split()))
K = int(input())


dp = np.array([[False for i in range(K+1)]for i in range(n+1)])

if __name__ == '__main__':
    dp[0][0] = True
    for i in range(n):
        for j in range(K+1):
            for k in range(m[i]+1):    
                if k*a[i] <= j:
                    dp[i+1][j] |= dp[i][j-k*a[i]]
            if dp[i][j] == True and dp[i+1][j] == False:
                dp[i+1][j] = True    
            
    print(dp[n][K])
