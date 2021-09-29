def lista_de_coefs():
    coefs = list(map(float, input().split()))
    return coefs


def poli_para_deriv(coefs):
    contador = 0
    for n in range(0, len(coefs)):
        derivada = n * coefs[n]
        if contador != 0:
            print(f"{derivada:.4f}")
        contador = contador + 1


def main():
    coefs = lista_de_coefs()
    poli_para_deriv(coefs)


main()
