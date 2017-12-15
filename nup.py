n = 4
w = [2,1,3,2]
v = [3,2,4,2]
W = 5

def rec (i,j):
    
    if i == n:
        return 
    elif j < w[i]:
        return rec(i+1,j)
    else:
        res = max(rec(i+1,j),rec(i+1,j-w[i])+v[i])
        return res

print(rec(0,W))
print(res)
         