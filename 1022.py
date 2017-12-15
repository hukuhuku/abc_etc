from collections import Counter

S = input()
s = list(S)

counter = Counter(s)
odd = 0
flag = True

for k,v in counter.items():
    #偶奇性の判定
    if k != 'x':
        if v%2 == 1:
            odd += 1
            mid = k
    if odd >= 2:#奇数個ある小文字が複数ある場合できない
        flag = False

#"x"を除いた時の回文判定
if flag:
    s_sub = S.replace("x","")
    if odd == 1:
        indexes = [i for i,x in enumerate(s_sub)if x == mid]
        center = indexes[len(indexes)//2 ]#奇数個ある数の中央のindexをとる
        if s_sub[center-1::-1] != s_sub[center+1:]:
            flag = False
    else:
        center = len(s_sub)//2
        if s_sub[center-1::-1] != s_sub[center:]:
            flag = False
        else:
            mid = s_sub[center]

#各アルファベットの距離判定
    if flag:
        indexes = [i for i,x in enumerate(s) if x == mid]
        if odd == 1:
            center = indexes[len(indexes)//2]
                        
            count = 0
            hidari = []
            migi = []

            for i in range(0,center)[::-1]:
                if s[i] == 'x':
                    count += 1
                else:
                    hidari.append(count)
                    count = 0
    
            hidari.append(count)
            count = 0

            for i in range(center+1,len(s)):
                if s[i] == 'x':
                    count += 1
            
                else:
                    migi.append(count)
                    count = 0

            migi.append(count)
            count = 0

            ans = 0
        elif odd == 0:
            a = indexes[len(indexes)//2]
            b = indexes[len(indexes)//2]
            ans = 0
            count = 0
            hidari = []
            migi = []

            if (b-a)%2 != 0:
                ans += 1
            
            for i in range(0,a)[::-1]:
                if s[i] == 'x':
                    count += 1
                else:
                    migi.append(count)
                    count = 0
            migi.append(count)
            count = 0
            for i in range(b,len(s)):
                if s[i] == 'x':
                    count += 1
                else:
                    hidari.append(count)
                    count = 0
            hidari.append(count)
        for i in range(len(hidari)):
            ans += abs(hidari[i]-migi[i])
        print(ans)
    else:
        print(-1)

else:
    print(-1)
            
            

