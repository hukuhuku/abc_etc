N = int(input())
#%%

es = [[] for i  in range(N)]
dic = {}
res = [0 for i in range(N)]
count = [0 for i in range(N)]
rear = 0
x = []
y = []


for i in range(N-1):                                    #辞書の要素にリストを渡したいので、一度それぞれリストに格納する。。
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    es[a].append((b,c))
    es[b].append((a,c))

for s in range(N):
    dic[s] = es[s]

Q,K = list(map(int,input().split()))
K -= 1

for w in range(Q):
     u,v= list(map(int,input().split()))
     x.append(u)
     y.append(v)

def dfs(k):
    global rear
    for l in range(len(dic[k])):
        nx = dic[k][l][0]
        if nx == rear:
            res[nx] += count[nx]
        else:
            count[nx] += dic[k][l][1]+count[k]
            res[nx] = count[nx]
            rear = nx
            dfs(nx)

dfs(K)
for m in range(Q):
    print(res[x[m]] + res[y[m]])
