n = int(input())
d = {}

for i in range(n):
    k = input()
    v = int(input())
    d[k] = v

kq = {}
for k in d:
    if d[k] > 50:
        kq[k] = d[k]

print(kq)
