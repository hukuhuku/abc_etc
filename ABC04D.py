def dfs(nokori,queue,ans,center):
    if ans == 0:
        center += 1000#-1000~1000までの配列を0~2000までの配列に補正したい。
        flag[center] = True
        queue.insert(0,center+1)
        queue.insert(0,center-1)
        nokori -= 1
    
    if nokori == 0:
        return ans

    a = queue.pop()

    if flag[a] == False:
        flag[a] = True
        ans += abs(a-center)
        nokori -= 1
        if a < center:#左側に広がっている場合さらに左に進むように
            queue.insert(0,a-1)
        else :#上と同じ
            queue.insert(0,a+1)
    return dfs(nokori,queue,ans,center)

if __name__ == "__main__":
    R,G,B = list(map(int,input().split()))
    flag = [False for i in range(2000)]
    ans = 0

    
    T = [R,G,B]
    T = sorted(T)[::-1]
    for i in T:
        queue = []
        if T == R:
            ans += dfs(R,queue,0,-100)
        elif T == G:
            ans += dfs(G,queue,0,0)
        else:
            ans += dfs(B,queue,0,100)

    print(ans)