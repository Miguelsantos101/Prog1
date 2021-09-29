def somar_seqs(A, B, total):
    sobra = 0

    for alpha in range(len(A) - 1, - 1, - 1):

        if sobra == 0:
            soma_temp = A[alpha] + B[alpha]
        else:
            soma_temp = A[alpha] + B[alpha] + sobra
            sobra = sobra - 1

        if soma_temp >= 10:
            sobra = sobra + 1
            soma_temp = soma_temp - 10
            total.append(soma_temp)
        else:
            total.append(soma_temp)

        if alpha == 0 and sobra == 1:
            total.append(sobra)


def main():
    seq_a = list(map(int, input().split()))
    seq_b = list(map(int, input().split()))
    total = list()
    somar_seqs(seq_a, seq_b, total)
    for beta in range(len(total) - 1, -1, -1):
        print(total[beta], end=" ")


main()
