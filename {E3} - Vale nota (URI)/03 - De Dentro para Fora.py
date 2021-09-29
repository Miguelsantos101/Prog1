def substituidor(comeco, lista, chave, leitor=True):
    if leitor:
        fim = len(lista) // 2
    else:
        fim = len(lista)
    for beta in range(comeco, fim):
        lista[beta] = chave[fim - (beta + 1)]


def decifrador(palavra):
    div = (len(palavra) // 2)
    l_comeco = palavra[:div]
    l_fim = palavra[div:]

    substituidor(0, palavra, l_comeco)
    substituidor(div, palavra, l_fim, False)

    palavra = "".join(palavra)
    print(palavra)


def main():
    N = int(input())
    for alpha in range(N):
        palavra = list(input())
        decifrador(palavra)


main()

# def decifrador(palavra):
#     div = (len(palavra) // 2)
#     comeco = palavra[:div]
#     fim = palavra[div:]
#     palavra_decifrada = palavra
#     for beta in range(0, len(comeco)):
#         palavra_decifrada[beta] = comeco[len(comeco) - (beta + 1)]
#     for gamma in range(len(comeco), len(palavra)):
#         palavra_decifrada[gamma] = fim[len(palavra) - (gamma + 1)]
#     palavra_decifrada = "".join(palavra_decifrada)
#     print(palavra_decifrada)
#
#
# def main():
#     N = int(input())
#     for alpha in range(0, N):
#         palavra = list(input())
#         decifrador(palavra)
#
#
# main()
