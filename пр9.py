def maxf():
    n = int(input())
    if n == 0:
        return -1
    max1 = maxf()
    return max(n, max1)
maxff = maxf()
print(maxff)
