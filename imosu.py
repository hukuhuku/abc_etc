'''1gen

C = [1,2,3,4,5,6,7]
T = [3,4,5,6,7,8,9]

table = [0 for i in range(max(T)+1)]

for i in range(len(C)):
    table[C[i]] += 1
    table[T[i]] -= 1

ans = 0
people = 0

for j in range(len(table)):
    people += table[j]
    ans = max(ans,people)

print(ans)

'''
N,W,H = list(map(int,input().split()))
tiles = [[0 for i in range(W+1)] for i in range(H+1)]
for _ in range(N):
    a,b,c,d = map(int,input().split())
    tiles[a] += 1
    tiles[b] -= 1
    tiles[c] -= 1
    tiles[d] += 1

ans = 0

for i in range(H+1):
    for j in range(W):
        tiles[i][j+1] += tiles[i][j]
        if ans < tiles[i][j+1]:
            ans = tiles[i][j+1]

        

