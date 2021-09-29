n = int(input())
M = [[0] * n for _ in range(n)]

eixoX = 1
eixoY = 0
linha = 0
coluna = 0
guarda_l = linha
guarda_c = coluna
troca = 0

for alpha in range(1, (n ** 2) + 1):

    if eixoX == 1 and troca == 0 and coluna < n:

        if M[linha][coluna] == 0:
            M[linha][coluna] = alpha
            coluna += 1
            guarda_l = linha
            guarda_c = coluna

        else:
            eixoX = 0
            eixoY = 1
            troca = 1

    elif eixoX == 1 and troca == 0 and coluna == n:

        coluna -= 1















for i in range(len(M)):
    for j in range(len(M)):
        print(M[i][j], end="\t")
    print("")
