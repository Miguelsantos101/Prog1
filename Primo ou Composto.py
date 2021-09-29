X = int(input())
n = 1
resto = 0

while n <= X:
    if X % n == 0:
        resto = resto + 1
    n = n + 1

if resto == 2:
    print("Primo")
else:
    print("Composto")
