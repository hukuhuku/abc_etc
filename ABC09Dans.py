import numpy as np

#pythonではむりげーっぽい
def dot_bit (g_1,g_2):
    res = [[0 for i in range(K)] for j in range(K)]
    for i in range(K):
        for j in range(K):
            for m in range(K):
                res[i][j] ^= g_1[i][m]&g_2[m][j]
 
    return np.array(res,dtype='int64')
        

K,M = list(map(int,input().split()))
A = list(map(int,input().split()))
C = list(map(int,input().split()))

A = np.array([A[::-1]],dtype='int64')
C = np.array([C],dtype='int64')
eye = np.eye(K-1,K,dtype='int64')           #K*K-1の単位行列的なものを作成
G = np.r_[C,eye]
m = bin(M-K)[2:]                            #適当
m = m[::-1]

m = np.array(list(m))
count = 0

if m[0] == '1':
    Power = G
    count = 1

for k in range(1,len(m)):
    G = dot_bit(G,G)
    

    
    if m[k] == '1':
        if count == 0:
            Power = G
            count += 1
            
        else:
            Power = dot_bit(G,Power)
            
    print(Power)
ans = Power[0][0]&A[0][0]
for i in range(1,K):
    ans ^= Power[0][i]&A[0][i] 

print(ans)





