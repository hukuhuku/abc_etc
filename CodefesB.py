N,M,K = list(map(int,input().split()))

res = 'No'

for i in range(N+1):
    for j in range(M+1):
        if i*(M-j) + j*(N-i) == K:
            res = 'Yes'
            break

print(res)            

