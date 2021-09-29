N = int(input())

fib = 0
X = 0
Y = 1
Z = X + 1

while fib < N - 1:
    Z = X + Y
    X = Y
    Y = Z
    fib += 1

print(Z)

N = int(input())
F_1 = 0
F_2 = 1
F_3 = F_1 + F_2
for i in range(0, N-1):
    F_3 = F_1 + F_2
    F_1 = F_2
    F_2 = F_3
if N != 0:
    print(F_3)
else:
    print(F_1)
