import collections

N = int(input())
A = list(map(int,input().split()))
A = sorted(A)[::-1]

s = collections.Counter(A)
res = 1
count = 0

for i in list(set(A)):
    if 4 <= s[i] and count != 1:
        res *= i
        res *= i
        count += 2
    elif 2 <= s[i]:
        res *= i 
        count += 1

    if count == 2:
        break

if count == 2:
    print(res)
else:
    print(0)
    

