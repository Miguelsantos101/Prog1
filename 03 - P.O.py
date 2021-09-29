n = int(input())
valor = []
peso = []
valor.append(list(map(int, input().split())))
peso.append(list(map(int, input().split())))
W = int(input())
total = 0

while total <= W:
    for alpha in range(n):
        for beta in range(n):
            total = valor[alpha][beta] + valor[alpha][beta + 1]
