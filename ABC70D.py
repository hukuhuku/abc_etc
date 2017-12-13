#%%

N = int(input())


es = [[]for i in range(N)]
dic = {}
res = [0 for i in range(N)]
count = [0 for i in range(N)]
rear = 0
x = []
y = []

for i in range(N-1):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    es[a].append((b,c))
    es[b].append((a,c))
for s in range(N):
    dic[s] = es[s]

Q,K = list(map(int,input().split()))
K -= 1

for w in range(Q):
    u,v = list(map(int,input().split()))
    x.append(u)
    y.append(v)
#%%
