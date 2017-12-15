#L = int(input())
#n = int(input())
#x = list(map(int,input().split()))


L = 10
n = 3
x = [2,6,7]


maxT = []
minT = []
for i in range(n):
  maxT.append(max(x[i],(L-x[i])))
  minT.append(min(x[i],(L-x[i])))



print(max(maxT))
print(max(minT))
