def calc(a,b):
    #x+y+z=a,x*y*z=bを想定
    for x in range(1,a-1):
        for y in range(1,a-x):
            z = a-x-y
            print(x,y,z)
            if x*y*z == b:
                return x,y,z
res =calc(3,1)
print(res)