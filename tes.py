N,M = list(map(int,input().split()))
A = []
D = []

for i in range(N):
    a,b = list(map(int,input().split()))
    A.append(a)
for j in range(M):
    c,d = list(map(int,input().split()))
    D.append(d)

A = sorted(A)
D = sorted(D)
count = 0

for i in range(len(A)):
    for j in range(len(D)):
        if D[j] <= A[i]:
            count += 1
            break
        
        D.pop(j)
print(count)