def lista():
    vetor = list(map(float, input().split()))
    return vetor


def main():
    U = lista()
    V = lista()
    produto = 0

    for i in range(len(U)):
        produto = produto + (U[i] * V[i])

    print(f"{produto:.4f}")


main()

# Versão resumida sem funções:
#
# U = list(map(float, input().split()))
# V = list(map(float, input().split()))
# produto = 0
#
# for X in range(0, len(U)):
#     produto = produto + (U[X] * V[X])
#
# print(f"{produto:.4f}")
