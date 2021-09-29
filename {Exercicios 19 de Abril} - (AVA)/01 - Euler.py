X = float(input())
N = int(input())

E = 0.0
for exp in range(0, N+1):

    fatorial = 1
    for numero in range(1, exp+1):
        fatorial = fatorial * numero

    E = E + X ** exp / fatorial

print(f"{E:.4f}")
