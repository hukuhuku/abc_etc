from collections import Counter
from collections import defaultdict 

N,M = map(int,input().split())
dict = defaultdict(set)

for i in range(M):
    a,b = list(map(int,input().split()))  
    dict[a].add(b)
    dict[b].add(a)



color = [0 for i in range(N+1)]
res = True

def dfs(v,c,queue=[]):
    u'''
    v : 現在のグラフの頂点
    c : 現在参照するフラグ,1=>-1=>1と使うので渡す必要がある
    queue : 探索したグラフの頂点を入れていく
    res : global変数を使いたくないが,再帰のreturnがよくわからないのでとりあえず
    '''

    global color
    global res 
    queue.append(v)
    
    for i in list(dict[v]):
        if color[i] == c:#隣の頂点が同じ値を与えられている際Falseを返す
            res = False
        elif i not in queue:#探索済みでなければ再帰する
            color[i] = c*-1#0ならcとは異なる値を格納
            dfs(i,-c,queue)#引数に-cとすることで,cが1=>-1=>1を繰り返す


color[1] = 1#始点色分けする
dfs(1,1)

if res:
    counter = Counter(color)
    B = counter[1]
    W = counter[-1]
    print(B*W-M)

else:
    print(int(N*(N-1)/2 - M))
    
            
