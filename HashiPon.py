v,e = list(map(int,input().split()))
dic = {}
for j in range(e):
    a,b = list(map(int,input().split()))
    dic[a].append(b)
    dic[b].append(a)

for i in range(v):
    if dic[i] 