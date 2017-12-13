H,W,T = list(map(int,input().split()))
s = [[] for i in range(H)]
count = [[9999999999 for i in range(W)] for j in range(H)]
path = [[0 for i in range(W)] for j in range(H)]
count[0][0] = 0

#ダイクストラ法？（メモ化再帰のつもりでやってた）
#移動方向を以前の場所以外の3か所にしたい。移動前の座標を参照しないような条件付け
#移動マスを数えたい。

for j in range(H):
    s[j] = list(input()) 
    if "S" in s[j]:
        sx = j
        sy = s[j].index("S")
    if "G" in s[j]:
        gx = j
        gy = s[j].index("G")

def dik(x,y,a,b):
    for i in range(4):
        dx,dy = x+[0,1,0,-1][i] ,y+[1,0,-1,0][i]
        nx,ny = x+dx,y+dy
        if s[nx][ny] != s[x+a][y+b]:
            if 0 <= nx and nx <　W and　0 <= ny and ny < H :
                if s[nx][ny] == "#" :
                    if count[x][y] + 1 < count[nx][ny]:
                        count[nx][ny] = count[x][y]+1
                elif s[nx][ny] == "G":                      #最初についた時点で終わってしまう。
                    return
                else:
                    count[nx][ny] = count[x][y]

                if count[x][y] <= count[nx][ny]:
                    path[nx][ny] = path[x][y] + 1                    
                dic(nx,ny,-dx,-dy)
            
count[gx][gy]
res = (T + count[gx][gy] - path[gx][gy])/count[gx][gy]
res = int(res)
print(res)
#できそうにないので次やる