N = int(input())
n = 2025 - N
ans = []

for i in range(1,10):
    if (n/i)%1 == 0 and (n/i) < 10:
        ans.append(str(i) + ' x ' + str(int(n/i)))


for r in ans:
    print(r)