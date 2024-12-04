def sort_ryad(ryad):
    return sorted(ryad)
with open('KosyanenkoVyacheslavAndreevich_VVOD.txt', 'r') as infile:
    n = int(infile.readline().strip())
    m = int(infile.readline().strip())
    mat = []
    for i in range(n):
        ryad1 = infile.readline().strip()
        ryad = list(map(int, ryad1.split()))
        mat.append(sort_ryad(ryad))
with open('KosyanenkoVyacheslavAndreevich_VIVOD.txt', 'w') as outfile:
    for ryad in mat:
        outfile.write(' '.join(map(str, ryad)) + '\n')
