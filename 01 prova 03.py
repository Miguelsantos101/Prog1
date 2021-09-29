def fazer_matriz(n, M):

    def alterar_matriz_principal(x, l_atual, c_atual, cont):
        contador = cont
        if x == 12:
            contador, l_atual, c_atual = fazerL(l_atual, c_atual, contador)
        if x == 21:
            contador, l_atual, c_atual = fazerU(l_atual, c_atual, contador)
        if x == 24:
            contador, l_atual, c_atual = fazerX(l_atual, c_atual, contador)

        return contador, l_atual, c_atual

    def fazerL(l_atual, c_atual, cont):
        if c_atual % 2 == 0:
            c_atual += 1

        for beta in range(0, 4):
            M[l_atual][c_atual] = cont

            if beta == 0:
                l_atual += 1
                c_atual -= 1

            elif beta == 1:
                c_atual += 1

            elif beta == 2:
                l_atual -= 1
                c_atual -= 1

            cont += 1

        return cont, l_atual, c_atual

    def fazerU(l_atual, c_atual, cont):
        if c_atual % 2 != 0:
            c_atual -= 1

        for gamma in range(0, 4):
            M[l_atual][c_atual] = cont

            if gamma == 0:
                l_atual += 1

            elif gamma == 1:
                c_atual += 1

            elif gamma == 2:
                l_atual -= 1

            cont += 1

        return cont, l_atual, c_atual

    def fazerX(l_atual, c_atual, cont):
        if c_atual % 2 != 0:
            c_atual -= 1

        for delta in range(0, 4):
            M[l_atual][c_atual] = cont

            if delta == 0:
                l_atual += 1
                c_atual += 1

            elif delta == 1:
                c_atual -= 1

            elif delta == 2:
                l_atual -= 1
                c_atual += 1

            cont += 1

        return cont, l_atual, c_atual

    m = (n - 2) // 4
    M_aux = [[0] * (2 * m + 1) for _ in range(2 * m + 1)]
    # (Começo do Código) Até aqui ele descobre o valor de m e cria uma matriz auxiliar

    for a1 in range(len(M_aux)):
        for b1 in range(len(M_aux)):

            if a1 < m + 1:
                M_aux[a1][b1] = 12
            if a1 == m + 1:
                M_aux[a1][b1] = 21
            if a1 > m + 1:
                M_aux[a1][b1] = 24
    # # A matriz auxiliar é preenchida corretamente

    M_aux[len(M_aux) // 2][len(M_aux) // 2] = 21
    M_aux[len(M_aux) // 2 + 1][len(M_aux) // 2] = 12
    # # Trocar o L do meio da matriz auxiliar com U abaixo dela

    l_atual = 0
    c_atual = n // 2
    guarda_l = l_atual
    guarda_c = c_atual
    contador = 1

    subM_l_atual = 0
    subM_c_atual = len(M_aux) // 2
    subM_guarda_l = subM_l_atual
    subM_guarda_c = subM_c_atual
    subM_limit = n // 2

    for alpha in range(0, subM_limit ** 2):

        if alpha >= 1:
            l_atual -= 2
            c_atual += 2

            subM_l_atual -= 1
            subM_c_atual += 1

        if l_atual < 0:
            l_atual = n - 2

        if c_atual >= n:
            c_atual = 0

        if subM_l_atual < 0:
            subM_l_atual = subM_limit - 1

        if subM_c_atual > subM_limit - 1:
            subM_c_atual = 0

        if M_aux[subM_l_atual][subM_c_atual] != 0:
            subM_guarda_l = subM_l_atual
            subM_guarda_c = subM_c_atual
            guarda_l = l_atual
            guarda_c = c_atual
            x = M_aux[subM_l_atual][subM_c_atual]
            M_aux[subM_l_atual][subM_c_atual] = 0
            contador, l_atual, c_atual = alterar_matriz_principal(x, l_atual, c_atual, contador)

        else:
            subM_l_atual = subM_guarda_l + 1
            subM_c_atual = subM_guarda_c
            l_atual = guarda_l + 2
            c_atual = guarda_c
            x = M_aux[subM_l_atual][subM_c_atual]
            M_aux[subM_l_atual][subM_c_atual] = 0
            contador, l_atual, c_atual = alterar_matriz_principal(x, l_atual, c_atual, contador)


def imprimeM(n, M):
    for i in range(n):
        for j in range(n):
            print(M[i][j], end="\t")
        print("")


def main():
    n = int(input())
    M = [[0] * n for i in range(n)]
    fazer_matriz(n, M)
    imprimeM(n, M)


main()
