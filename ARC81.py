N = int(input())
S1 = list(input())
S2 = list(input())
i = 0


if S1[i] != S2[i]:
    res = 6
    i+=2
    rear = 1
else :
    res = 3
    i+=1
    rear = 0

while i != N:
    if S1[i] != S2[i]:
        if rear == 1:
            res *= 3
        else:
            res *= 2
        rear = 1
        i += 2

    else:
        if rear == 0:
            res *= 2
        i += 1
        rear = 0


print(res%1000000007)
        
        
