X = int(input())

exp = 0
bin = 0

while X != 0:
    mod = X % 2
    bin = bin + mod * 10 ** exp
    exp = exp + 1
    X = X // 2

print(bin)
