N = int(input())
a = [1,2,4,7]
k = int(input())
A = [0 for i in range(N*2)]
sum = 0
res = 'NO'
resint = 0

def bubunwa(n,a,k):
    for i in range(n):
        A.append(a[i+sum])
        if sum(A) == k:
            res = 'YES'
            resint = A
            break

    sum += 1


    A = []
    return bubunwa(m,a,k)



print (res)
print(resint)
