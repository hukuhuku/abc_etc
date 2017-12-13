N = int(input())
A = list(map(int,input().split()))

ans = 0
count = 0

for i in range(N):
    if A[i] != 0:
        ans += A[i]
        count += 1
