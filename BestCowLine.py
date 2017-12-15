N = 6
S = "ACDBCB"

S_list = list(S)
S_Last = N
queue = []

for i in range(N):
    if S_Last == 0:
        queue.append(S_list[0])
    elif S_list[0] < S_list[S_Last]:   #maxでどちらかを選ぶをやるとコードが短くなりそう
        queue.qppend(S_list.pop(0))
        S_Last -= 1
    elif S_list[0] > S_list[S_Last]:
        queue.qppend(S_list.pop(S_Last))
        S_Last -= 1

print (queue)
