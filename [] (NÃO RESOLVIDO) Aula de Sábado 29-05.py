def main():
    N = int(input())
    medidas = list(map(int, input().split()))
    verificador(medidas)


def verificador(medidas):
    padrao = True
    l_picos_vales = []
    primeiro_valor = 0
    for alpha in range(len(medidas)):
        if alpha == 0:
            primeiro_valor = medidas[alpha]
        if alpha != 0:
            pico(medidas[alpha], medidas[alpha - 1], l_picos_vales, padrao)
            vale(medidas[alpha], medidas[alpha - 1], l_picos_vales, padrao)
    l_picos_vales.insert(0, primeiro_valor)

    for beta in range(len(l_picos_vales)):
        if l_picos_vales[beta] == "errado":
            padrao = False

    print(1 if padrao else 0)


def pico(medida_n, medida_anterior, l_picos_vales, padrao):
    if medida_n > medida_anterior:
        l_picos_vales.append("pico")
        return

    if medida_n == medida_anterior:
        l_picos_vales.append("errado")
        return


def vale(medida_n, medida_anterior, l_picos_vales, padrao):
    if medida_n < medida_anterior:
        l_picos_vales.append("vale")
        return l_picos_vales

    if medida_n == medida_anterior:
        l_picos_vales.append("errado")
        return


main()

# 3
# 1 4 -2
#
# 5
# 100 99 112 -8 -7
#
# 4
# 1 2 2 1