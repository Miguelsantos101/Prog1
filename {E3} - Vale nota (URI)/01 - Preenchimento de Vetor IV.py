def add_par_ou_impar(n, lista_par, lista_impar):
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)


def main():
    lista_par = []
    lista_impar = []
    for i in range(0, 15):
        n = int(input())
        add_par_ou_impar(n, lista_par, lista_impar)
        if len(lista_par) == 5:
            for alpha in range(0, 5):
                print(f"par[{alpha}] = {lista_par[alpha]}")
            lista_par = []
        if len(lista_impar) == 5:
            for beta in range(0, 5):
                print(f"impar[{beta}] = {lista_impar[beta]}")
            lista_impar = []
    for o in range(0, len(lista_impar)):
        print(f"impar[{o}] = {lista_impar[o]}")
    for p in range(0, len(lista_par)):
        print(f"par[{p}] = {lista_par[p]}")


main()
