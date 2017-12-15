
#%%

n = 5
a = [100,3,2,3,4,5,10]
a.sort()

max_len = 0

for i in range(n)[::-1]:
        j = i-1
        if a[i] < (a[j] + a[j-1]):
            max_len = (a[i] + a[j] + a[j-1])
            break

print(max_len)
