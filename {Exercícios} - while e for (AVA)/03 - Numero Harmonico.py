X = int(input())

harmonico = 1

for i in range(2, X+1):
    harmonico = harmonico + 1 / i

print(f"{harmonico:.4f}")
