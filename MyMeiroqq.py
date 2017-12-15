#nx,ny = 現在の座標
#gx,gy = ゴールの位置

maze = [
    ['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
    ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#'],
    ]

INF = 10000000

xlen = len(maze)
ylen = len(maze[0])

dis = [[INF for i in range(xlen)] for j in range(ylen)]

for i in range(xlen):
    for j in range(ylen):
        if maze[i][j] == 'G':
            gx,gy = i,j
        elif maze[i][j] == 'S':
            sx,sy = i,j
queue = []

def bfs():
    queue.insert(0,(sx,sy))
    distance[sx][sy] = 0
    while len(queue):
        x,y = queue.pop()
        if x == gx and y == gy:
            return distance[x][y]

        for k in range(0,4):
            dx,dy =  x + [0,1,0,-1][k] , y+ [1,0,-1,0][k]
            if (0 <= dx and dx < xlen and 0 <= dy and dy < ylen and maze[dx][dy] == '.' and distance[x][y] < distance[dx][dy]): 
                queue.insert(0,(dx,dy))　　　　　　　　　　　　　　　　　　　　　　　　　　
                distance[dx][dy] = distance[x][y] +1                                                                            
res = bfs()
print(res)
