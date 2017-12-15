def comb(n,m):
    res = 1
    for i in range(m):
        res *= (n-i)/(i+1)
    return res
print(comb1(10,3))