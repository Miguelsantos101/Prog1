n = int(input())

coordenadas = []
M = [[0] * n for _ in range(n)]

for alpha in range(n):
    coordenadas.append(list(map(int, input().split())))




for i in range(len(M)):
    for j in range(len(M)):
        print(M[i][j], end="\t")
    print("")
