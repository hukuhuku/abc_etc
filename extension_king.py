import numpy as np
K = int(input())
N = int(input())
x = np.array([])

for i in range(N):
    x = np.append(list(map(int,input().split())),i)
