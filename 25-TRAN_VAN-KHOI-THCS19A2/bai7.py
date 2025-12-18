n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

k = int(input())

for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == k:
            print(a[i], a[j])
