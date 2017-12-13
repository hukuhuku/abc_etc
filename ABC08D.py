import itertools

W,H = map(int,input().split())#0<=x<=H,0<=y<W
N = int(input())
X = []
Y = []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
        
A = list(itertools.permutations(range(N),N))

for i in range(len(A)):
    memo = [[False for k in range(H)]for k in range(W)]
    for j in range(N):
        
