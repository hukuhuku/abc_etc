n,k = map(int,input().split())

x = []
y = []
point = []

for _ in range(n):
    X,Y = map(int,input().split())
    x.append(X)
    y.append(Y)
    point.append((X,Y))

x = sort(x)
y = sort(y)

res = 10**20

for a in x:
    for b in x:
        ci = 0
        di = 1
        while di < len(y):
            num = 0
            c = y[ci]
            d = y[di]

            for i in point:
                if a <= i[0] <= b and c <= i[1] <= d:
                    num += 1
            
            if num >= K:
                res = min(res,abs(b-a)*abs(d-c))
                if ci < di:
                    ci += 1
                else:
                    di += 1
            else:
                di += 1
print(res)

