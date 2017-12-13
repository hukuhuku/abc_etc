N = int(input())
c = []
for i in range(N):
    c.append(int(input()))
v = [1 for i in range(N)]


for i in range(1,N):

    for j in range(i):
        if 0 < c[i]-c[j]:
            v[i] = max(v[i],v[j]+1)
print(N-max(v))
        
        
