from collections import Counter

#リストの各値を数えてくれる
D = [1,2,2,2,2,2,2,1,1]
counter = Counter(D)

from collections import defaultdict

#辞書のValueに配列を入れやすい
#引数にsetなどを指定することも可能
G = defaultdict(list)
G[1].add(22)

from collections import deque
#pop(0)など配列の先頭削除の遅延を解決できる

queue = deque()
queue.qppedndleft(1)#先頭に1を挿入する
