def bfs():
    ans = 0
    queue = []
    queue.insert(0,[0,0,0])

    while len(queue):
        x,y,n = queue.pop(0)
        if N <= n:
            if x == X and y == Y:
                ans += 1
        else:
            n += 1
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx = x+dx
                ny = y+dy
                queue.insert(0,[nx,ny,n])
    return ans


N,D = map(int,input().split())
X,Y = map(int,input().split())

if X%D == 0 and Y%D == 0:
    X /= D
    Y /= D
    ans = bfs()
    print(ans/4**N)
else:
    print(0.0)