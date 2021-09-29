# URI: 1101 - Sequência de Números e Soma

M = 1
N = 1
soma = True

while M > 0 and N > 0:
    M, N = map(int, input().split())
    if M <= 0 or N <= 0:
        break
    elif M > N:
        soma = N
        while M != N:
            print(N, end=" ")
            Y = N + 1
            soma = soma + Y
            N = N + 1
        print(f"{N} Sum={soma}")
    elif N > M:
        soma = M
        while N != M:
            print(M, end=" ")
            Z = M + 1
            soma = soma + Z
            M = M + 1
        print(f"{M} Sum={soma}")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# URI: 1117 - Validação de Nota

nota = -1
contador = 1
X = 0
Y = 0
media = 0

while nota > 10 or nota < 0:
    nota = float(input())
    if nota > 10 or nota < 0:
        print("nota invalida")
    elif contador == 1 and 10 >= nota >= 0:
        X = nota
        nota = -1
        contador = contador + 1
    elif contador > 1 and 10 >= nota >= 0:
        Y = nota
        media = (X + Y) / 2
        nota = 0
        print(f"media = {media:.2f}")





for y in range(1, 11):
    for x in range(1, 11):
        print(f'{y} X {x} = {y * x}')