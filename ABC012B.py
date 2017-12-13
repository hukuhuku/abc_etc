N = int(input())

h = N//(60**2)
m = (N-h*60*60)//60
s = (N-h*60*60)%60

h = str(h).zfill(2)
m = str(m).zfill(2)
s = str(s).zfill(2)

print(h+":"+m+":"+s)