
def debug_print(field=[[]]):
    for i in range(len(field)):
        print (field[i])
        print("\n")




def lake_counting(field):
    debug_print(field)

    xlen = len(field)
    ylen = len(field[0])

    lake_count = 0

    def dfs(x,y):
        field[x][y] = '.'               #座標（ｘ，ｙ）のWを。にする
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:         #周囲8マスを探索する
                nx = x + dx
                ny = y + dy
                if (0 <= nx and nx < xlen ):　　
                    if (0 <= ny and ny < ylen):
                        if(field[nx][ny] == "W"): #周囲8マスに文字列が存在した場合、中心を移動させて再帰する
                            dfs(nx,ny)

    for i in range(0,xlen):
        for j in range(0,ylen):
            if(field[i][j] == 'W'):    #dfsにより文字列のカウントが行われるのが最初に見つかった一度のみとなる（それ以外は書き換えられる）
                dfs(i,j)
                lake_count += 1
    return lake_count


b

print (lake_counting(field))
