s = input()

cnt = 0
ans = 0

if len(s) == 1:
    cnt = 0
else:
    l = 0
    k = len(s)-1
    while True:
        if s[l] == s[k]:
            l += 1
            k -= 1
            if l + k >= 
            