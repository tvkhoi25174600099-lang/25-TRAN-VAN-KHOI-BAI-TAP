d = {}
n = int(input())

for i in range(n):
    k = input()
    v = input()
    d[k] = v

d2 = {}
for k in d:
    d2[d[k]] = k

print(d2)
