N = 3
D = [[3,2,1],[2,2,1],[1,1,1]]
Q = 3
P = [1,4,9]

dq = [[0]*(N+1) for i in range(N+1)]

for i in range(N)[::-1]:
    for j in range(N)[::-1]:
        dq[i][j] =  dq[i+1][j] + dq[i][j+1] - dq[i+1][j+1] + D[i][j]
#DP


score = [0] * (N ** 2 + 1)

for i in range(N):#0 T N-1
    for j in range(N):# 0 T N-1
        for k in range(i + 1,N + 1):
            for l in range(j + 1,N + 1):
                s = (k - i)* (l - j)
                score[s] = max(score[s],dq[i][j] - dq[k][j] - dq[i][l] + dq[k])
for i in range(1,len(score)):
    score[i] = max(score[i -1], score[i])

for i in P:
    print(score[i])
