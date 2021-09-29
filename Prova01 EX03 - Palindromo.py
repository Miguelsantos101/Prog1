palindromo = int(input())
M = palindromo
W = 0
while M > 0:
    W = W * 10 + M % 10
    M = M // 10
if palindromo == W:
    print("SIM")
else:
    print("NAO")
