N,M = list(map(int,input().split()))
dic = {}
x = [[]for i in range(13)]
queue = []

for i in range(M):
    a,b = list(map(int,input().split()))
    x[a].append(b)
    x[b].append(a)

for i in range(1,13):
    dic[i] = x[i]

res = 0
count = 0
flag = True
queue = []

def dfs(i,j,list):
    global count
    global flag
    print(list,i,j)
    if i == N :
        count = (max(j,count))
        return
    if dic[i] == []:
        flag = False
    for k in dic[i]:
        for l in list:
            if l not in dic[k]:
                flag = False
                break
    if flag:
        list.append(i)
        dfs(i+1,j+1,list)
    else:
        dfs(i+1,j,list)
        flag = True
    

dfs(1,0,queue)


print(count)



