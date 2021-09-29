X = float(input())
K = int(input())

cos = 1.0
op = 0

for exp in range(2, K + 1, 2):

    fatorial = 1

    for numero_fat in range(exp, 0, -1):
        fatorial = fatorial * numero_fat

    if op % 2 == 0:
        cos = cos - (X ** exp / fatorial)

    elif op % 2 != 0:
        cos = cos + (X ** exp / fatorial)

    op = op + 1

print(f"{cos:.4f}")
