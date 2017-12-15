from collections import Counter

N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

res = 'YES'
counter_d = Counter(D)
counter_t = Counter(T)

set_t = list(set(T))
for i in set_t:
    if counter_d[i] < counter_t[i]:
        res = 'NO'
        break

print(res)

print(Counter(T) - Counter(D) and 'NO' or 'YES')
