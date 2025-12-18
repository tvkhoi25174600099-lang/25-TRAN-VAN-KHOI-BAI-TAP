n = int(input())
tong = 0

for i in range(n):
    for j in range(n):
        x = int(input())
        if i == j:
            tong += x

print(tong)
