###Proteobacteria門とBacteroidete門の各網名を取得


Bactero = []
index = []
allindex = []
#indexには順に同じ網に所属するもののindexを持ち,allindexに渡す
#Bacteroには網名を記録させる

for i in range(len(kpc[1])):
    if kpc[1][i] == "Bacteroidetes":
        if kpc[2][i] not in Bactero:
            Bactero.append(kpc[2][i])
            allindex.append(index)
            index = []
        
        index.append(i)
allindex.pop(0)#データがないNanが入っていたので取り出したい
Bactero.pop(0)

bdict = {}
index = -1
for i in Bactero:
    index += 1
    bdict[i] = allindex[index]

Proteo = []
index = []
allindex = []
#indexには順に同じ網に所属するもののindexを持ち,allindexに渡す
#Bacteroには網名を記録させる

for i in range(len(kpc[1])):
    if kpc[1][i] == "Proteobacteria":
        if kpc[2][i] not in Proteo:
            Bactero.append(kpc[2][i])
            allindex.append(index)
            index = []
        
        index.append(i)


pdict = {}
index = -1
for i in Proteo:
    index += 1
    pdict[i] = allindex[index]