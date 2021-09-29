a, b, c = map(int, input().split())

A = a
B = b
C = c

X = int()

if A > B:
    X = A
    A = B
    B = X

if A > C:
    X = A
    A = C
    C = X

if B > C:
    X = B
    B = C
    C = X

print(f"{A}\n{B}\n{C}\n\n{a}\n{b}\n{c}")
