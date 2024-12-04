f = open("17-1.txt")
a = list(map(int, f ))
maxs = -10*10
k = 0
for i in range(len(a)-1):
    if (a[i] % 3 == 0) and (a[i+1] % 3 == 0):
        k += 1
        maxs = max(maxs, a[i] + a[i+1])


