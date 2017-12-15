a = int(input())
b = int(input())

res = abs(a-b)

if abs(10-a)+abs(b-0) < res:
    res = abs(10-a)+abs(b-0)
print(res)