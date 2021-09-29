X = int(input())

exp = 0
dec = 0

while X != 0:
    mod = X % 10
    dec = dec + mod * 2 ** exp
    exp = exp + 1
    X = X // 10

print(dec)
