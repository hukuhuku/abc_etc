N = int(input())
K = int(input())
x = list(map(int,input().split()))

res = 0

for i in range(N):
    res += 2*min(x[i]-0,abs(x[i]-K))

print(res)