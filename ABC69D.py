    H,M = list(map(int,input().split()))
    N = int(input())
    a = list(map(int,input().split()))


    #spaceによって一元配列を作成しそれを折りたたむように２元配列に組み立てる。

    space = []
    mass = [[0 for i in range(M)] for j in range(H)]　　#M*H次元配列の作成
    count = 0


    for i in range(N):
        for j in range(a[i]):
            space.append(i+1)                          #a[i]の数だけi＋１をspaceに加える。



    for k in range(H):
        for n in range(M):
            mass[k][n] = str(space[count])
            count += 1

    for l in range(H):　　　　　　　　　　　　　　　　　　　#奇数行目の配列を逆向きにする。
      if l%2 == 1:
          mass[l].reverse()


    for x in range(H):
      print(" ".join(mass[x]))　　　　　　　　　　　　　　#””.joinにより、配列を空白区切りで出力する。
