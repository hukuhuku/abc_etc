N = int(input())

#4/N = 1/w + 1/h + 1/n
#h,w,nを求める

def calc(b,a=4):
    #x+y+z=a,x*y*z=bを想定
    for x in range(1,a-1):
        for y in range(1,a-x):
            z = a-x-y
            if x*y*z == b:
                print(x,y,z)
                return x,y,z

def p():
    if N%4 == 0:
        return [1,2,4]
    elif N%2 == 0:
        return [1,2]
    else:
        return [1]

a = p()
for i in a:
    if calc(int(N/i)):
        res = calc(int(N/i))
        break

print(k) 
