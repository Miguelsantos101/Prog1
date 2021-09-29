A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

pares = 0
positivos = 0
impares = 0
negativos = 0

if A > 0:
    positivos = positivos + 1
elif A < 0:
    negativos = negativos + 1
if A % 2 == 0:
    pares = pares + 1
else:
    impares = impares + 1

if B > 0:
    positivos = positivos + 1
elif B < 0:
    negativos = negativos + 1
if B % 2 == 0:
    pares = pares + 1
else:
    impares = impares + 1

if C > 0:
    positivos = positivos + 1
elif C < 0:
    negativos = negativos + 1
if C % 2 == 0:
    pares = pares + 1
else:
    impares = impares + 1

if D > 0:
    positivos = positivos + 1
elif D < 0:
    negativos = negativos + 1
if D % 2 == 0:
    pares = pares + 1
else:
    impares = impares + 1

if E > 0:
    positivos = positivos + 1
elif E < 0:
    negativos = negativos + 1
if E % 2 == 0:
    pares = pares + 1
else:
    impares = impares + 1

print(f"{pares} valor(es) par(es)\n{impares} valor(es) impar(es)\n{positivos} valor(es) positivo(s)\n"f"{negativos} valor(es) negativo(s)")
