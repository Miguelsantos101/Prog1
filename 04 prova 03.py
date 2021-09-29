n = int(input())
lista_de_letras = []

for alpha in range(n):
    lista_de_letras.append(list(map(str, input().split())))

k = int(input())

palavra = []


for beta in range(k):
    linha = 0
    coluna = 0
    soma = 0
    encontrada = 0
    x = input()

    for letra in x:
        palavra.append(letra)

    for gamma in range(n ** 2):
        for delta in range(n ** 2):

            if palavra[gamma] in lista_de_letras[gamma][delta]:
                soma += 1

                if soma == len(palavra):
                    encontrada += 1

    print(f"{x}: {encontrada}")
















for i in range(len(lista_de_letras)):
    for j in range(len(lista_de_letras)):
        print(lista_de_letras[i][j], end="\t")
    print("")
