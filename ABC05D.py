N = int(input())
D = []
for i in range(N):
    D.append(list(map(int,input().split())))
Q = int(input())
P = []
for i in range(Q):
    P.append(int(input()))

dp = [[0 for i in range(N+1)] for i in range(N+1)]  #N+1*N+1とることでdp[N][N]を求めやすくする

###右下から始まる長方形の面積を求める##
for i in range(N)[::-1]:
    for j in range(N)[::-1]:
        dp[i][j] = dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1] + D[i][j]#Nから0まで下りていくので,i+1はひとつ前のものを参照している。

res = [0 for i in range(N**2 + 1)]

###最大値の探索###
for i in range(N):
    for j in range(N):
        for k in range(i+1,N+1):#iの値より右にある座標を参照
            for l in range(j+1,N+1):#jより下の座標を参照
                s = (k-i)*(l-j)
                res[s] = max(res[s],dp[i][j] - dp[k][j] - dp[i][l] + dp[k][l])

###最大値の更新###
for i in range(1,len(res)):
    res[i] = max(res[i-1],res[i])

for i in P:
    print(res[i])