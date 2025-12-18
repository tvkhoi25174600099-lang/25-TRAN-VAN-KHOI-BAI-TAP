n = int(input())
m = int(input())

max_sum = None
hang_max = -1

for i in range(n):
    tong = 0
    for j in range(m):
        tong += int(input())
    if max_sum is None or tong > max_sum:
        max_sum = tong
        hang_max = i

print(hang_max)

