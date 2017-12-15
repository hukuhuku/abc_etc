Name_H,N = list(map(int,input().split()))
H = []
for i in range(N-1):
    H.append(int(input()))

H.append(Name_H)
H.sort(reverse=False)

H = H[::-1]
res = H.index(Name_H)+1

if res%10 == 1:
    print(str(res)+"st")
elif res%10 == 2:
    print(str(res)+"nd")
elif res%10 == 3:
    print(str(res)+"rd")
else:
    print(str(res)+"th")