N,D = map(int,input().split())
X,Y = map(int,input().split())

if X%D == 0 and Y%D == 0:
    X = X/D
    Y = Y/D
else:
    res = 0.0
