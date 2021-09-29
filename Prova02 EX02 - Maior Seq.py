# ANALISAR CASO A CASO
def maior_seq(list):
    maior_seq = 0

    for a in range(len(list)):
        if a == 0:
            maior_seq = list[a]

        fixo = list[a]
        valor_seq = fixo

        # VERIFICAR SE CHEGOU NO ULTIMO
        if a + 1 == len(list):
            break

        # LADO DIREITO
        if a + 1 < len(list) - 1:
            prox = list[a + 1]
            maior_d = prox
            soma_d = 0

            for b in range(a + 1, len(list)):
                soma_d += list[b]

                if soma_d > maior_d:
                    maior_d = soma_d

            if maior_d > 0:
                valor_seq += maior_d

        # LADO ESQUERDO
        if a - 1 >= 0:
            ant = list[a - 1]
            maior_e = ant
            soma_e = 0

            for b in range(a - 1, -1, -1):
                soma_e += list[b]

                if soma_e > maior_e:
                    maior_e = soma_e

            if maior_e > 0:
                valor_seq += maior_e

        if valor_seq > maior_seq:
            maior_seq = valor_seq

    # FINALMENTE FORA
    print(maior_seq)


def main():
    listona = list(map(int, input().split()))
    maior_seq(listona)


main()
