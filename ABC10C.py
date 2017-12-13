import math
a,b,c,d,T,V = map(int,input().split())
n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]

res = "NO"
for i in range(n):
    iki = math.sqrt((a-xy[i][0])**2+(b-xy[i][1])**2)
    kae = math.sqrt((xy[i][0]-c)**2+(xy[i][1]-d)**2)
    if iki+kae <= V*T:
        res = "YES"
        break
print(res)