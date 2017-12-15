#gx,gy == ゴールの座標の位置
#maze  == 迷路のあれ

### 迷路は合流などしないものとしてもいいっぽい
###　合流がある場合は３３行付近で大きさ比較にすればいいのかな？


def clear_maze(sx,sy,gx,gy,maze):
    INF = 10000000000

    xlen = len(maze)
    ylen = len(maze[0])

    distance =[[INF for i in range(xlen)] for j in range(ylen)]
    # disrance = [[None]*xlen]*ylen

    def bfs():
        queue = []

        queue.insert(0,(sx,sy))
        distance[sx][sy] = 0                #最初の座標の位置から現時点の位置を初期化し、ひとつのマス移動するごとに１ずつ増やしていく。

        while len(queue):                   #queueがある間実行を行う
            x,y = queue.pop()

            if x == gx and y == gy:           #ゴールの位置に来ている時に実行を中止する０
                break

            for i in range(0,4):
                nx,ny = x + [1,0,-1,0][i], y+[0,1,0,-1][i]

                if (0<=nx and nx<xlen and 0 <= ny and ny < ylen and maze[nx][ny] == INF and distance[nx][ny] = INF):
                    queue.insert(0,(nx,ny))
                    distance[nx][ny] = distance[x][y] + 1

        return distance[gx][gy]


print(clear_maze(0,1,9,8,maze))
