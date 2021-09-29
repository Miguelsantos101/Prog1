T = int(input())

for testes in range(0, T):
    anos = 0
    PA, PB, G1, G2 = map(str, input().split())
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)

    while PA <= PB and anos <= 100:
        PA = PA + int(((PA * G1) / 100))
        PB = PB + int(((PB * G2) / 100))
        anos = anos + 1
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")
