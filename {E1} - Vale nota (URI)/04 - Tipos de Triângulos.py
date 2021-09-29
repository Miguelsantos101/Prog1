a, b, c = map(float, input().split())

X = float()

if a < b:
    X = a
    a = b
    b = X

if a < c:
    X = a
    a = c
    c = X

if b < c:
    X = b
    b = c
    c = X

A = a
B = b
C = c

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if A * A == (B * B + C * C):
        print("TRIANGULO RETANGULO")
    if A * A > (B * B + C * C):
        print("TRIANGULO OBTUSANGULO")
    if A * A < (B * B + C * C):
        print("TRIANGULO ACUTANGULO")

if A == B and A == C and B == C:
    print("TRIANGULO EQUILATERO")
else:
    if A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
