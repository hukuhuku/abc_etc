N = int(input())
a = list(map(int,input().split()))

count = 0
a.append(0)
C = 0
res = 0

for i in range(N):      #ひとつずつ確かめていく
    if a[i] < a[i+1]:
        count += 1　　　
        C += count      #n番目の連続が見つかった時、それ以前の組み合わせに（ｎ−１)を足す。

    else :
        res += C
        C = 0           #リセットが必要
        count = 0

print(res+N)　　　　　　
