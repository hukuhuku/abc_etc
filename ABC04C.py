N = int(input())
num = ["1","2","3","4","5","6"]
n = N%30
m = n//5
s = n%5

for i in range(m):
    a = num.pop(0)
    num.append(a)

for i in range(s):
    k = num[i]
    p = num[i+1]
    num[i] = p
    num[i+1] = k

print("".join(num))