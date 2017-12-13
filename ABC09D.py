K,M = list(map(int,input().split()))
A = list(map(int,input().split()))
C = list(map(int,input().split()))




for j in range(K-1,M):
    a = 0
    for i in range(K):
        a ^= C[i]&A[j-i]

    A.append(a)

print(A[M-1])

