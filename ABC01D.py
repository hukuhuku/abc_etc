N = int(input())
Max = 24*60//5+1
time = [False for i in range(Max)]

res_start = []
res_end = []
flag = True

def rain(a):
    
    global flag
    if flag:
        flag = False
        res_start.append(a)

    if time[a+1]:
        rain(a+1)
        time[a+1] = False
    else:
        flag = True
        res_end.append(a+1)




for i in range(N):
    s,e = list(map(int,input().split("-")))
    start = (s//100*60 + s%100 - s%5)//5         #start = 左二桁*60 + 右二桁 - 丸見込み誤差
    end = (e//100*60 + e%100 + (5 - e%5)%5)//5
    for j in range(start,end):
        time[j] |= True

for i in range(Max):
    if time[i]:
        res_start.append(i)
        for j in range(i,Max+1):
            if time[j] == False:
                res_end.append(j)
                break
            time[j] = False


for i in range(len(res_start)):
    res_start[i] = (res_start[i]*5//60)*100 + res_start[i]*5%60
    res_end[i] = (res_end[i]*5//60)*100 + res_end[i]*5%60

for i in range(len(res_start)):
    print("{:04d}-{:04d}".format(res_start[i], res_end[i]))

