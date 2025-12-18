n = int(input())
d = {}

for i in range(n):
    k = input()
    v = int(input())
    d[k] = v

max_key = None
max_val = None

for k in d:
    if max_val is None or d[k] > max_val:
        max_val = d[k]
        max_key = k

print(max_key)
