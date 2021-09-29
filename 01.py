N = int(input())

for alpha in range(N):
    linha = list(input())

    for beta in range(len(linha)):
        atual = linha[beta]

        for gamma in range(len(linha)):
            if atual == linha[gamma]:
                if atual.isalpha:
