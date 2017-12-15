S = list(input())
a = ["a","i","u","e","o"]
res = []


for i in range(len(S)):
    if S[i] not in a:
        res.append(S[i])

print("".join(res))



