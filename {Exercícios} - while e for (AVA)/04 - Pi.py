X = int(input())

pi = 4
op = 0

for div in range(3, X+1, 2):
    if op % 2 == 0:
        pi = pi - 4 / div
    elif op % 2 != 0:
        pi = pi + 4 / div
    op = op + 1

print(f"{pi:.4f}")
