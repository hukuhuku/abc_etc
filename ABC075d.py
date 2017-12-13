from itertools import combinations as comb

def count(x1,y1,x2,y2):
    res = 0
    for x,y in point:
        if x1 <= x <= x2 and y1 <= y <= y2:
            res += 1
    return res 
    
N,K = map(int,input().split())

x = []
point = []
y_dict = {}

for i in range(N):
    a,b = map(int,input().split())
    x.append(a)
    point.append((a,b))
    y_dict[a] = b#yの値はxの値と紐づけしておく

x = sorted(x)
ans = 10**20

number = [i for i in range(N)]
C = list(comb(number,2))

for i,j in C:#組合せで調べる
    y_list = []

    for k in range(i,j+1):#xの指定区間内にある点のy座標を取得しy_listに入れる
        y_list.append(y_dict[x[k]])
        
    y_list = sorted(y_list)
        

    if 2 <= len(y_list):
        number2 = [i for i in range(len(y_list))]
        C_2 = list(comb(number2,2))

        for l,m in C_2:        
                x1 = x[i]
                y1 = y_list[l]
                x2 = x[j]
                y2 = y_list[m]
                n = count(x1,y1,x2,y2)#区間内の点の数
                   
                if K <= n :
                    ans = min(ans,(x2-x1)*(y2-y1)) 
               
print(ans) 






