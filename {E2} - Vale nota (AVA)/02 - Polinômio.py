def lista():
    vetor = list(map(float, input().split()))
    return vetor


def main():
    coefs = lista()
    K = int(input())
    for n in range(0, K):
        valordopolinomio = 0
        X = float(input())
        for c in range(0, len(coefs)):
            valordopolinomio = valordopolinomio + (coefs[c] * (X ** c))
        print(f"{valordopolinomio:.4f}")


main()
