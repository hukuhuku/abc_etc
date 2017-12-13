N,M = list(map(int,input().split()))
x = []
y = []
red = [0 for i in range(N)]
#appendでやるよりも代入してやったほうが0.6倍くらい必要時間が減る
mas = [1 for i in range(N)]
red[0] = 1

for i in range(M):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    mas[x] -= 1
    mas[y] += 1
    if red[x] == 1:
        if red[y] == 0:
            red[y] = 1
        if mas[x] == 0:
            red[x] = 0

print(sum(red))

        
    
