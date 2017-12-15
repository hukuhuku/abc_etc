import datetime
from datetime import timedelta

n = int(input())
today = datetime.date(2017,4,1)
ans = []
for i in range(n):
    y,m,d = map(int,input().split())
    date = datetime.date(y,m,d)
    res = today - date
    ans.append(res.days)

for i in range(n):
    print(ans[i])
