N,M = list(map(int,input().split()))

if 2*N>M or 4*N<M:
    a = -1
    b = -1
    c = -1
else:
    b = M%2
    c = int(((M-3*b)-2*(N-b))/2)
    a = N-b-c
print(a,b,c)