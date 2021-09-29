A = list(map(str, input().split(', ')))
B = list(map(str, input().split(', ')))

AxB = list()
linha = list()

pares_iguais = list()
XmaiorY = list()
XmenorY = list()


for i in range(0, len(A)):
    for n in range(0, len(B)):
        par_ordenado = [A[i], B[n]]
        linha.append(par_ordenado)

    AxB.append(linha[:])
    linha.clear()

for a in AxB:
    print(a)
    for par in a:
        if par[0] == par[1]:
            pares_iguais.append(par)
        elif par[0] > par[1]:
            XmaiorY.append(par)
        elif par[0] < par[1]:
            XmenorY.append(par)

print(f'\nPara X = Y: {pares_iguais}\nPara X > Y:{XmaiorY}\nPara X < Y:{XmenorY}')