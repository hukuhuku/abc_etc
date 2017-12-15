def __logging(visited,rest=[]):
    if rest:              #restが存在する場合に真となる
        print "visited:%s\n rest:%s\n" %(visited,rest)　
    else:
        print "visited:%s" %(visited)

is_fined = False　　　　　　#グローバル変数としてis_finedを定義する。

def dfs_rec(graph,start,end,visited=[]):
    global is_fined　　　　#グローバル変数のis_finedを指定する。
    if is_fined:
        return visited
    if start == end:　#startは配列
        is_fined = True #次回の繰り返しで終了
        visited.append(start)
        __logging(visited) #配列を表示する
        return visited

    visited.append(start)
    __logging(visited)

    for label in graph.get(start,[]):　#labelがstart番目の配列を取得
        if not label in visited:　　　　#まだ探索していない場合真となる
            visited = dfs_rec(graph,label,end,visited)　#start(1)→label(2→3→4…)の順で実行

    return visited

if __name__ == '__main__': #モジュールがトップレベルで実行される場合にテストできる
    graph = {1:[2,6,8],
             2:[3,4],
             3:[],
             4:[5],
             5:[1],
             6:[7],
             7:[],
             8:[9,10],
             9:[7],
             10:[11],
             11:[],
             }
    print dfs_rec(graph,1,10)
