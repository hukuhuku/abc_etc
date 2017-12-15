#n = int(input())
#a = list(map(int,input().split()))
#k = int(input())





n = 4
k = 15
a = [1,2,4,7]


def Psum (N,A,K):
    res = 'NO'
    for l in range(N):  #実行を0~N目から行う
        A = []
        for i in range(l,N):　
            A.append(a[i]) #(l~N)番目の要素を追加する
            if sum(A) == k: #Aの和がｋのとき
                res = 'Yes'
    print(res)





Psum(n,a,k)
