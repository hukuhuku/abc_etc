s = list(input())
count = 0
l = 0
r = len(s)-1

#リストsの先頭と末尾を比較
#先頭と末尾がx以外で異なるなら,-1を返す。
#先頭と末尾が同じなら先頭と末尾を移動させる。
#どちらか片方がxなら片方にxを追加し先頭と末尾を移動させたとするので最初にxだったほうだけ移動させる

#xabxa
while l != r:
    if s[l] != s[r]:
        if s[l] != "x" and s[r] != "x":
            count = -1
            break
        elif s[l] == "x" and s[r] != "x":
            l += 1
            count += 1
        elif s[r] == "x" and s[l] != "x":
            r -= 1
            count += 1
    elif s[l] == s[r]:
        if abs(l-r) == 1:
            break
        else:
            l += 1
            r -= 1

print(count)
