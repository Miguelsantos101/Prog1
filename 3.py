L = int(input())
T = input()

linha = 0
coluna = 0
soma = 0
media = 0
contador = 0

M = [[0] * 12 for _ in range(12)]
for alpha in range(144):
    entrada = float(input())
    M[linha][coluna] = entrada
    coluna += 1
    if coluna > len(M) - 1:
        coluna = 0
        linha += 1
    if linha > len(M) - 1:
        linha = 0






for i in range(len(M)):
    for j in range(len(M)):
        print(M[i][j], end="\t")
    print("")











for beta in range(len(M)):
    soma += M[L][contador]
    contador += 1

if T == "S":
    print(soma)
if T == "M":
    print(f"{soma / len(M):.1f}")
