A,B = map(int,input().split())
res = 0
 
for i in range(B+1):
    if '4' in list(str(i))  or '9' in list(str(i)):
        res += 1
print(res)
count = 0
for i in range(A):
    if '4' in list(str(i))  or '9' in list(str(i)) :
        res -= 1
        count += 1
print(count)
 
print(res)