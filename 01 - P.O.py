n = int(input())

M = []
numeros = []
repetidos = []
numero_de_repeticoes = []

for alpha in range(n):
    M.append(list(map(int, input().split())))

for beta in range(n):
    for gamma in range(n):
        numeros.append(M[beta][gamma])

numeros.sort()

for delta in range(n ** 2):
    atual = numeros[delta]
    if atual in repetidos:
        pass
    else:
        repetidos.append(atual)
        numero_de_repeticoes.append(numeros.count(atual))

x = 0
maior_rep = 0
guarda_maior_rep = []

while x < len(numero_de_repeticoes):

    if x == 0:
        guarda_maior_rep.append(x)
        maior_rep = numero_de_repeticoes[x]
    elif numero_de_repeticoes[x] > maior_rep:
        maior_rep = numero_de_repeticoes[x]
        guarda_maior_rep = []
        guarda_maior_rep.append(x)
    elif numero_de_repeticoes[x] == maior_rep:
        guarda_maior_rep.append(x)
    x += 1

for repetido in guarda_maior_rep:
    print(repetidos[repetido])
