def calc(n):
    for k in [3,2,1]:
        if n-k not in NG:
            return n-k
    return 300

N = int(input())
NG = []
M = N
for i in range(3):
    NG.append(int(input()))

for _ in range(100):
    N = calc(N)


if M in NG:
    print("NO")
elif N <= 0:
    print("YES")
else:
    print("NO")

