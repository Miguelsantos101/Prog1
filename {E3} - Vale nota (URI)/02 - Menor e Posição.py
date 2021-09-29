def main():
    menor_val = pos = True
    N = int(input())
    vetor = list(map(int, input().split()))
    for alpha in range(0, N):
        if alpha == 0:
            menor_val = vetor[alpha]
            pos = alpha

        else:
            if menor_val > vetor[alpha]:
                menor_val = vetor[alpha]
                pos = alpha

    print(f"Menor valor: {menor_val}")
    print(f"Posicao: {pos}")


main()
