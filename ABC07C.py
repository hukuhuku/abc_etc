INF = 10**9+7

R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
c = [list(input())for i in range(R)]
distance = [[INF for i in range(C)]for i in range(R)]
queue = [[sy-1,sx-1]]
distance[sy-1][sx-1] = 0

def bfs():
    global distance
    global queue

    while len(queue):
        y,x = queue.pop(0)
        for ny,nx in [[1,0],[0,1],[-1,0],[0,-1]]:
            dy = y + ny
            dx = x + nx
            
            if 0 <= dx <= C and 0<= dy <= R and c[dy][dx] == '.' and distance[y][x]+1 < distance[dy][dx]:
                queue.append([dy,dx])
                distance[dy][dx] = distance[y][x] + 1

bfs()
print(distance[gy-1][gx-1])
