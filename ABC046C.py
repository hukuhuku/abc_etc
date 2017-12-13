N,M = list(map(int,input().split()))
A = []
B = [[]for i in range(N)]
C = []
D = [[]for i in range(M)]
male ={}
fema = {}

for i in range(N):
    a,b = list(map(int,input().split()))
    if a in A :
        B[A.index(a)].append(b)
    else:
        A.append(a)
        B[i].append(b)    
for i in range(M):
    c,d = list(map(int,input().split()))
    if c in C:
        D[C.index(x)].append(d)
    else:
        C.append(c)
        D[i].append(d)
for i in range(len(A)):
    male[A[i]] = B[i]
for i in range(len(C)):
    fema[C[i]] = D[i]


