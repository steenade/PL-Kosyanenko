def sort_ryad(ryad):
    return sorted(ryad)
n = int(input())
m = int(input())
mat = []
for i in range(n):
    ryad1 = input("Строка " + str(i + 1) + ": ")
    ryad = list(map(int, ryad1.split()))
    mat.append(sort_ryad(ryad))
for ryad in mat:
    print(ryad)