n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

k = int(input())
k = k % n

b = []
for i in range(n):
    b.append(a[n - k + i] if i < k else a[i - k])

print(b)
