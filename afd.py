N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

A = list(set(A))
A = sorted(A)
print(A)
print(A[-1])