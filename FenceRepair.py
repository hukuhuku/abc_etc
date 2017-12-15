N = 5
L = [10,4,5,1,2]


cost = -min(L)
for i in range(N):
    for j in range(len(L)):
        if L[j] == max(L):
            cost += sum(L)
            L.pop(j)
            break

print(cost)
