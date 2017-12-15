def calc(W,H,N,M):
    """
    W:ゲームフィールドのx方向の長さ
    H:ゲームフィールドのy方向の長さ
    N:金融回収マシンの数
    M:マシンのx,y座標
    """
    
    X = [None for _ in range(len(M))]
    Y = [None for _ in range(len(M))]

    #マシンのx座標,y座標それぞれを配列X,Yに格納する
    for i in range(len(M)):
        X[i] = M[i][0]
        Y[i] = M[i][1]

    memo = {}

    def dp(l,r,t,b):
        #left,right,top,bottom
