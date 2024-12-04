def proverka(n):
    if n <= 1:
        return "NO"
    for i in range(2, n):
        if n % i == 0:
            return "NO"
    return "YES"
n = int(input())
print(proverka(n))



