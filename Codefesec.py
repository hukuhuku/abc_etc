N,M = list(map(int,input().split()))
G = [[] for i in range(N+1)]
for i in range(M):
    a,b = list(map(int,input().split()))
    G[a].append(b)
    G[b].append(a)

