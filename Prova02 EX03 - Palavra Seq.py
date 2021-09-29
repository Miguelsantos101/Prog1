def imprimir_indices(indices):
    for j in range(len(indices)):
        print(indices[j])


def analisar_frase(fra, pala):
    palavra_encontrada = False
    indices = []

    for i in range(len(fra)):
        alpha = i
        beta = alpha + len(pala)

        if pala == fra[alpha:beta]:
            indices.append(i)
            palavra_encontrada = True

    if not palavra_encontrada:
        print("NOT FOUND!")

    return indices


def main():
    frase = input()
    palavra = input()
    indices = analisar_frase(frase, palavra)
    imprimir_indices(indices)


main()
