from collections import deque
from collections import defaultdict
from collections import Counter

N,M = list(map(int,input().split()))
G = defaultdict(set)

color = [0 for i in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    G[A].add(B)
    G[B].add(A)

color[1] = 1
que = deque([1])
concatenation = False

while len(que):
    p = que.popleft()
    for q in list(G[p]):
        if color[q] == 0:
            color[q] = -color[p]
            que.append(q)
        elif color[q] == color[p]:
            concatenation = True
            break
    
if concatenation:
    print(N*(N-1)/2-M)
else:
    B = Counter(color)[1]
    W = Counter(color)[-1]
    print(B*W-M)
