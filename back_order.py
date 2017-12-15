N = int(input())
a = list(map(int,input().split()))

A = [[j,i+1] for i,j in enumerate(a)] #enumerateは一要素ごとに２つの値を返す。ひとつは添字、もうひとつは要素の値　ここではiに添字(index) jに値が入っている
A.sort(reverse=True)                  #Aの値について降順でソートする。

for k in range(N):
  print(A[k][1])　　　　　　　　　　　　　#2番目の要素がindexなのでそれを表示する。
