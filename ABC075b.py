H,W = map(int,input().split())
S = []
res = [[0 for i in range(W)]for i in range(H)]

for i in range(H):
    s = list(input())
    S.append(s)

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            res[i][j] = '#'
            for x,y in [[j-1,i-1],[j,i-1],[j+1,i-1],[j-1,i],[j+1,i],[j-1,i+1],[j,i+1],[j+1,i+1]]:
                if 0 <= x and 0 <= y and x <= W-1 and y <= H-1:
                    if res[y][x] != '#':
                        res[y][x] += 1
for i in range(H):
    for j in range(W):
        res[i][j] = str(res[i][j])
for i in range(H):
    print("".join(res[i]))
