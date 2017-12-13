Deg,Dis = list(map(int,input().split()))

direction = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
ws_list = [0.3, 1.6, 3.4, 5.5, 8.0, 10.8,13.9, 17.2, 20.8, 24.5, 28.5, 32.7]

res_speed = 0
res_direction = 'C'

Deg = (Deg + 112.5)
num = int(Deg/225)
if 15 < num:
    num = 0
    

round = lambda x:(x*2*10+1)//2/10
speed = round(Dis/60)

for i in ws_list[::-1]:
    if i <= speed:
        res_speed = ws_list.index(i)+1
        res_direction = direction[num]
        break

print(res_direction,res_speed)
