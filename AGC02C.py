#AC
N,L = list(map(int,input().split()))
a = list(map(int,input().split()))
a.append(0)
b = []
res = "Impossible"

for i in range(N):
    if L <= (a[i]+a[i+1]):　#Lよりも大きい箇所（二つ連続）があれば、適当に切っても条件は達成できる。
        count = i
        res = "Possible"
        break

if res =="Possible":
    for j in range(count):
        b.append(j+1)       #数の間を数えるので一つずらす。
    for k in range(count+1,N)[::-1]:
        b.append(k)
    
    print(res)
    for l in range(len(b)):
        print(b[l])
else:
    print(res)


