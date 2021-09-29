x = int(input())
y = int(input())
exp = 0

if y == 0:
    exp = 1
elif y == 1:
    exp = x
else:
    for alpha in range(y - 1):
        if alpha == 0:
            exp = x * x
        elif alpha > 0:
            exp = exp * x

print(exp)
